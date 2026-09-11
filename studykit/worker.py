from __future__ import annotations

import logging
import threading
import time
from pathlib import Path

from studykit.catalog.service import CatalogService
from studykit.compiler.llm import build_compiler
from studykit.config import get_settings
from studykit.db import get_session_factory, init_db
from studykit.domain.models import KitStatus
from studykit.domain.schema import KitSchema
from studykit.renderer.engine import render_kit
from studykit.storage.files import FileStore

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
log = logging.getLogger("studykit.worker")


def process_one() -> bool:
    settings = get_settings()
    session = get_session_factory()()
    catalog = CatalogService(session)
    store = FileStore(settings)
    compiler = build_compiler(settings)
    job = catalog.claim_job(settings.worker_id, settings.worker_lease_seconds)
    if not job:
        session.close()
        return False
    kit = catalog.get_kit(job.kit_id)
    if kit is None:
        catalog.finish_job(job, False, "kit missing")
        session.close()
        return True
    try:
        catalog.set_status(kit, KitStatus.compiling)
        source = store.read_source(kit.source_path)
        schema = compiler.compile(source, kit.original_filename)
        kit.schema_json = schema.model_dump()
        kit.title = schema.title
        session.add(kit)
        session.commit()

        catalog.set_status(kit, KitStatus.rendering)
        html = render_kit(schema, storage_key=f"studykit:{kit.id}")
        path = store.write_artifact(kit.id, html)
        kit.artifact_path = str(path)
        session.add(kit)
        session.commit()

        catalog.set_status(kit, KitStatus.review)
        catalog.finish_job(job, True)
        log.info("kit %s ready for review", kit.id)
    except Exception as exc:  # noqa: BLE001 — job must never kill the worker loop
        log.exception("job %s failed", job.id)
        catalog.set_status(kit, KitStatus.failed, str(exc))
        catalog.finish_job(job, False, str(exc))
    finally:
        session.close()
    return True


def run_loop(stop_event: threading.Event | None = None) -> None:
    settings = get_settings()
    log.info("worker %s polling every %ss", settings.worker_id, settings.worker_poll_seconds)
    while True:
        if stop_event is not None and stop_event.is_set():
            break
        try:
            did = process_one()
        except Exception:
            log.exception("claim loop failed")
            did = False
        if did:
            continue
        if stop_event is None:
            time.sleep(settings.worker_poll_seconds)
        elif stop_event.wait(settings.worker_poll_seconds):
            break


def run() -> None:
    init_db()
    run_loop()


def render_example_schema(schema_path: Path) -> str:
    schema = KitSchema.model_validate_json(schema_path.read_text(encoding="utf-8"))
    return render_kit(schema)


if __name__ == "__main__":
    run()
