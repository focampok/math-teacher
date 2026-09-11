from collections.abc import Generator
from datetime import UTC, datetime, timedelta

from fastapi import Depends, Header, HTTPException, Request
from sqlalchemy.orm import Session

from studykit.config import Settings, get_settings
from studykit.db import get_db
from studykit.storage.files import FileStore

_hits: dict[str, list[datetime]] = {}


def settings_dep() -> Settings:
    return get_settings()


def db_dep() -> Generator[Session, None, None]:
    yield from get_db()


def store_dep(settings: Settings = Depends(settings_dep)) -> FileStore:
    return FileStore(settings)


def require_token(
    settings: Settings = Depends(settings_dep),
    x_upload_token: str | None = Header(default=None),
    authorization: str | None = Header(default=None),
) -> None:
    provided = x_upload_token
    if not provided and authorization and authorization.lower().startswith("bearer "):
        provided = authorization[7:].strip()
    if not provided or provided != settings.upload_token:
        raise HTTPException(status_code=401, detail="invalid upload token")


def rate_limit(request: Request, settings: Settings = Depends(settings_dep)) -> None:
    ip = request.client.host if request.client else "unknown"
    now = datetime.now(UTC)
    window = now - timedelta(hours=1)
    stamps = [t for t in _hits.get(ip, []) if t > window]
    if len(stamps) >= settings.upload_rate_per_hour:
        raise HTTPException(status_code=429, detail="too many uploads from this address")
    stamps.append(now)
    _hits[ip] = stamps
