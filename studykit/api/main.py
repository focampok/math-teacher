from collections.abc import AsyncIterator
from contextlib import asynccontextmanager
from pathlib import Path

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from studykit import __version__
from studykit.api.routes_health import router as health_router
from studykit.api.routes_kits import router as kits_router
from studykit.api.routes_pages import router as pages_router
from studykit.db import init_db

WEB_STATIC = Path(__file__).resolve().parent.parent / "web" / "static"


@asynccontextmanager
async def lifespan(_app: FastAPI) -> AsyncIterator[None]:
    init_db()
    yield


def create_app() -> FastAPI:
    app = FastAPI(title="Studykit", version=__version__, lifespan=lifespan)
    app.include_router(health_router)
    app.include_router(pages_router)
    app.include_router(kits_router)
    if WEB_STATIC.is_dir():
        app.mount("/static", StaticFiles(directory=WEB_STATIC), name="static")
    return app


app = create_app()


def run() -> None:
    import uvicorn

    uvicorn.run("studykit.api.main:app", host="0.0.0.0", port=8000, reload=False)
