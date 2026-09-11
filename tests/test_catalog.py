from studykit.catalog.service import CatalogService, slugify
from studykit.db import get_session_factory
from studykit.domain.models import JobStatus, KitStatus


def test_slugify():
    assert slugify("Hola Mundo 2!") == "hola-mundo-2"


def test_claim_and_retry(client):
    # client fixture initializes the isolated DB
    session = get_session_factory()()
    catalog = CatalogService(session)
    kit, job = catalog.create_kit(filename="a.md", source_path="/tmp/a.md", title="A")
    claimed = catalog.claim_job("w1", 60)
    assert claimed is not None
    assert claimed.id == job.id
    assert claimed.status == JobStatus.running.value
    catalog.set_status(kit, KitStatus.failed, "boom")
    catalog.finish_job(claimed, False, "boom")
    retry = catalog.enqueue_retry(kit)
    assert retry.status == JobStatus.queued.value
    session.close()
