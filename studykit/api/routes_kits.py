from pathlib import Path

from fastapi import APIRouter, Depends, File, Form, HTTPException, UploadFile
from fastapi.responses import FileResponse, HTMLResponse
from sqlalchemy.orm import Session

from studykit.api.deps import db_dep, rate_limit, require_token, settings_dep, store_dep
from studykit.catalog.service import CatalogService
from studykit.config import Settings
from studykit.domain.models import KitStatus
from studykit.storage.files import FileStore

router = APIRouter()

_ALLOWED = {".md", ".txt", ".json"}
EXAMPLE_DIST = (
    Path(__file__).resolve().parents[2] / "examples" / "matematica-iv" / "dist" / "index.html"
)


def _catalog(db: Session) -> CatalogService:
    return CatalogService(db)


@router.post("/kits", status_code=201, dependencies=[Depends(require_token), Depends(rate_limit)])
async def upload_kit(
    file: UploadFile = File(...),
    db: Session = Depends(db_dep),
    store: FileStore = Depends(store_dep),
    settings: Settings = Depends(settings_dep),
):
    filename = file.filename or "source.md"
    suffix = Path(filename).suffix.lower()
    if suffix not in _ALLOWED:
        raise HTTPException(status_code=400, detail="only .md, .txt or .json files")
    data = await file.read()
    if not data:
        raise HTTPException(status_code=400, detail="empty file")
    if len(data) > settings.max_upload_bytes:
        raise HTTPException(status_code=413, detail="file too large (1 MB max)")
    catalog = _catalog(db)
    kit, job = catalog.create_kit(filename=filename, source_path="pending", title=Path(filename).stem)
    path = store.write_source(kit.id, filename, data)
    kit.source_path = str(path)
    db.add(kit)
    db.commit()
    db.refresh(kit)
    return {
        "id": kit.id,
        "job_id": job.id,
        "status": kit.status,
        "title": kit.title,
    }


@router.get("/kits/{kit_id}")
def kit_status(kit_id: str, db: Session = Depends(db_dep)):
    kit = _catalog(db).get_kit(kit_id)
    if kit is None:
        raise HTTPException(status_code=404, detail="kit not found")
    job = _catalog(db).latest_job(kit_id)
    return {
        "id": kit.id,
        "title": kit.title,
        "status": kit.status,
        "slug": kit.slug,
        "error": kit.error,
        "job": None
        if job is None
        else {"id": job.id, "status": job.status, "error": job.error},
    }


@router.get("/kits/{kit_id}/preview", dependencies=[Depends(require_token)])
def preview_kit(kit_id: str, db: Session = Depends(db_dep)):
    kit = _catalog(db).get_kit(kit_id)
    if kit is None:
        raise HTTPException(status_code=404, detail="kit not found")
    if kit.status not in {KitStatus.review.value, KitStatus.published.value}:
        raise HTTPException(status_code=409, detail="kit is not ready to preview")
    if not kit.artifact_path or not Path(kit.artifact_path).is_file():
        raise HTTPException(status_code=404, detail="artifact missing")
    return FileResponse(kit.artifact_path, media_type="text/html")


@router.post("/kits/{kit_id}/publish", dependencies=[Depends(require_token)])
def publish_kit(
    kit_id: str,
    slug: str | None = Form(default=None),
    db: Session = Depends(db_dep),
):
    catalog = _catalog(db)
    kit = catalog.get_kit(kit_id)
    if kit is None:
        raise HTTPException(status_code=404, detail="kit not found")
    try:
        kit = catalog.publish(kit, slug)
    except ValueError as exc:
        raise HTTPException(status_code=409, detail=str(exc)) from exc
    return {"id": kit.id, "slug": kit.slug, "status": kit.status, "url": f"/k/{kit.slug}"}


@router.post("/kits/{kit_id}/retry", dependencies=[Depends(require_token)])
def retry_kit(kit_id: str, db: Session = Depends(db_dep)):
    catalog = _catalog(db)
    kit = catalog.get_kit(kit_id)
    if kit is None:
        raise HTTPException(status_code=404, detail="kit not found")
    if kit.status != KitStatus.failed.value:
        raise HTTPException(status_code=409, detail="only failed kits can be retried")
    job = catalog.enqueue_retry(kit)
    return {"id": kit.id, "job_id": job.id, "status": kit.status}


@router.get("/k/{slug}")
def public_kit(slug: str, db: Session = Depends(db_dep), settings: Settings = Depends(settings_dep)):
    if slug == settings.example_slug and EXAMPLE_DIST.is_file():
        return FileResponse(EXAMPLE_DIST, media_type="text/html")
    kit = _catalog(db).get_by_slug(slug)
    if kit is None or kit.status != KitStatus.published.value:
        raise HTTPException(status_code=404, detail="kit not found")
    if not kit.artifact_path or not Path(kit.artifact_path).is_file():
        raise HTTPException(status_code=404, detail="artifact missing")
    return FileResponse(kit.artifact_path, media_type="text/html")


@router.get("/k/{slug}/generated")
def generated_example(
    slug: str,
    settings: Settings = Depends(settings_dep),
):
    """Renderer output for the golden Matemática IV schema (not the hand-built fallback)."""
    if slug != settings.example_slug:
        raise HTTPException(status_code=404, detail="no generated example")
    schema_path = EXAMPLE_DIST.parent.parent / "kit.schema.json"
    if not schema_path.is_file():
        raise HTTPException(status_code=404, detail="schema missing")
    from studykit.domain.schema import KitSchema
    from studykit.renderer.engine import render_kit

    schema = KitSchema.model_validate_json(schema_path.read_text(encoding="utf-8"))
    return HTMLResponse(render_kit(schema, storage_key=f"studykit:{slug}-generated"))
