from pathlib import Path

from fastapi import APIRouter, Depends, File, Form, HTTPException, Request, UploadFile
from fastapi.responses import FileResponse, HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

from studykit.api.deps import db_dep, settings_dep, store_dep
from studykit.api.routes_kits import publish_kit, retry_kit, upload_kit
from studykit.catalog.service import CatalogService
from studykit.config import Settings
from studykit.domain.models import Kit, KitStatus
from studykit.web.copy import BUSY, STATUS, STEPS, status_view

TEMPLATES = Jinja2Templates(
    directory=str(Path(__file__).resolve().parent.parent / "web" / "templates")
)

router = APIRouter()


def _base(settings: Settings, extra: dict | None = None) -> dict:
    ctx = {
        "steps": STEPS,
        "statuses": STATUS,
        "public_base": settings.public_base_url.rstrip("/"),
        "token": "",
        "error": None,
        "notice": None,
        "field_error": None,
        "flash_title": None,
        "flash_detail": None,
    }
    if extra:
        ctx.update(extra)
    return ctx


def _kit_ctx(kit: Kit, job, settings: Settings, extra: dict | None = None) -> dict:
    view = status_view(kit.status)
    ctx = _base(
        settings,
        {
            "kit": kit,
            "job": job,
            "view": view,
            "busy": kit.status in BUSY,
            "current_step": view["step"],
        },
    )
    if extra:
        ctx.update(extra)
    return ctx


@router.get("/", response_class=HTMLResponse)
def home(request: Request, db: Session = Depends(db_dep), settings: Settings = Depends(settings_dep)):
    kits = CatalogService(db).list_kits()
    return TEMPLATES.TemplateResponse(
        request,
        "home.html",
        _base(settings, {"kits": kits, "current_step": 1}),
    )


@router.get("/kits/{kit_id}/ui", response_class=HTMLResponse)
def kit_ui(
    kit_id: str,
    request: Request,
    db: Session = Depends(db_dep),
    settings: Settings = Depends(settings_dep),
    just: str | None = None,
):
    catalog = CatalogService(db)
    kit = catalog.get_kit(kit_id)
    if kit is None:
        raise HTTPException(status_code=404, detail="kit not found")
    extra = {}
    if just == "uploaded":
        extra = {
            "flash_title": "Archivo en cola",
            "flash_detail": "Ya lo tenemos. Esta página se actualiza sola cuando el kit esté listo para revisar.",
        }
    elif just == "published":
        extra = {
            "flash_title": "Publicado",
            "flash_detail": "Copia el enlace de abajo y compártelo con los alumnos.",
        }
    elif just == "retry":
        extra = {
            "flash_title": "Reintento en cola",
            "flash_detail": "Volvimos a mandar el archivo al worker.",
        }
    return TEMPLATES.TemplateResponse(
        request,
        "kit_admin.html",
        _kit_ctx(kit, catalog.latest_job(kit_id), settings, extra),
    )


@router.post("/ui/upload")
async def ui_upload(
    request: Request,
    token: str = Form(...),
    file: UploadFile = File(...),
    db: Session = Depends(db_dep),
    settings: Settings = Depends(settings_dep),
):
    kits = CatalogService(db).list_kits()
    if token != settings.upload_token:
        return TEMPLATES.TemplateResponse(
            request,
            "home.html",
            _base(
                settings,
                {
                    "kits": kits,
                    "current_step": 1,
                    "token": token,
                    "error": "El token no coincide con UPLOAD_TOKEN.",
                    "field_error": "token",
                },
            ),
            status_code=401,
        )
    try:
        result = await upload_kit(file=file, db=db, store=store_dep(settings), settings=settings)
    except HTTPException as exc:
        return TEMPLATES.TemplateResponse(
            request,
            "home.html",
            _base(
                settings,
                {
                    "kits": kits,
                    "current_step": 1,
                    "token": token,
                    "error": str(exc.detail),
                    "field_error": "file",
                },
            ),
            status_code=exc.status_code,
        )
    return RedirectResponse(url=f"/kits/{result['id']}/ui?just=uploaded", status_code=303)


@router.get("/ui/preview/{kit_id}")
def ui_preview(
    kit_id: str,
    request: Request,
    token: str | None = None,
    db: Session = Depends(db_dep),
    settings: Settings = Depends(settings_dep),
):
    if token != settings.upload_token:
        return TEMPLATES.TemplateResponse(
            request,
            "preview_gate.html",
            _base(
                settings,
                {
                    "kit_id": kit_id,
                    "current_step": 3,
                    "error": "Introduce el token para abrir el preview." if token else None,
                },
            ),
            status_code=401,
        )
    catalog = CatalogService(db)
    kit = catalog.get_kit(kit_id)
    if kit is None or kit.status not in {KitStatus.review.value, KitStatus.published.value}:
        raise HTTPException(status_code=409, detail="kit is not ready to preview")
    if not kit.artifact_path or not Path(kit.artifact_path).is_file():
        raise HTTPException(status_code=404, detail="artifact missing")
    return TEMPLATES.TemplateResponse(
        request,
        "preview_frame.html",
        _kit_ctx(kit, catalog.latest_job(kit_id), settings, {"token": token}),
    )


@router.get("/ui/preview/{kit_id}/raw")
def ui_preview_raw(
    kit_id: str,
    token: str | None = None,
    db: Session = Depends(db_dep),
    settings: Settings = Depends(settings_dep),
):
    if token != settings.upload_token:
        raise HTTPException(status_code=401, detail="invalid upload token")
    kit = CatalogService(db).get_kit(kit_id)
    if kit is None or kit.status not in {KitStatus.review.value, KitStatus.published.value}:
        raise HTTPException(status_code=409, detail="kit is not ready to preview")
    if not kit.artifact_path or not Path(kit.artifact_path).is_file():
        raise HTTPException(status_code=404, detail="artifact missing")
    return FileResponse(kit.artifact_path, media_type="text/html")


@router.post("/ui/publish/{kit_id}")
def ui_publish(
    kit_id: str,
    request: Request,
    token: str = Form(...),
    slug: str | None = Form(default=None),
    db: Session = Depends(db_dep),
    settings: Settings = Depends(settings_dep),
):
    catalog = CatalogService(db)
    kit = catalog.get_kit(kit_id)
    if kit is None:
        raise HTTPException(status_code=404, detail="kit not found")
    if token != settings.upload_token:
        return TEMPLATES.TemplateResponse(
            request,
            "kit_admin.html",
            _kit_ctx(
                kit,
                catalog.latest_job(kit_id),
                settings,
                {"field_error": "token", "token": token},
            ),
            status_code=401,
        )
    publish_kit(kit_id, slug=slug or None, db=db)
    return RedirectResponse(url=f"/kits/{kit_id}/ui?just=published", status_code=303)


@router.post("/ui/retry/{kit_id}")
def ui_retry(
    kit_id: str,
    request: Request,
    token: str = Form(...),
    db: Session = Depends(db_dep),
    settings: Settings = Depends(settings_dep),
):
    catalog = CatalogService(db)
    kit = catalog.get_kit(kit_id)
    if kit is None:
        raise HTTPException(status_code=404, detail="kit not found")
    if token != settings.upload_token:
        return TEMPLATES.TemplateResponse(
            request,
            "kit_admin.html",
            _kit_ctx(
                kit,
                catalog.latest_job(kit_id),
                settings,
                {"field_error": "token", "token": token},
            ),
            status_code=401,
        )
    retry_kit(kit_id, db=db)
    return RedirectResponse(url=f"/kits/{kit_id}/ui?just=retry", status_code=303)
