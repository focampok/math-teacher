from functools import lru_cache
from pathlib import Path

from pydantic import Field, field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict


def normalize_database_url(url: str) -> str:
    """Railway injects postgres://; SQLAlchemy+psycopg3 needs postgresql+psycopg://."""
    url = url.strip()
    if url.startswith("postgres://"):
        url = "postgresql://" + url.removeprefix("postgres://")
    if url.startswith("postgresql://"):
        url = "postgresql+psycopg://" + url.removeprefix("postgresql://")
    return url


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    database_url: str = "sqlite:///./data/studykit.sqlite"
    upload_token: str = "change-me"
    data_dir: Path = Path("./data")
    public_base_url: str = "http://127.0.0.1:8000"
    llm_api_key: str = ""
    llm_base_url: str = "https://api.openai.com/v1"
    llm_model: str = "gpt-4o-mini"
    llm_timeout_seconds: float = 60
    worker_poll_seconds: float = 2
    worker_lease_seconds: int = 180
    worker_id: str = "local-1"
    # Railway cannot mount one volume on two services. The web process polls the
    # Postgres queue itself unless you run a standalone worker and set this false.
    run_embedded_worker: bool = True
    max_upload_bytes: int = 1_000_000
    upload_rate_per_hour: int = 10

    example_slug: str = Field(default="matematica-iv")

    @field_validator("database_url", mode="before")
    @classmethod
    def _normalize_db(cls, value: str) -> str:
        return normalize_database_url(value) if isinstance(value, str) else value


def _ensure_sqlite_parent(url: str) -> None:
    if not url.startswith("sqlite"):
        return
    raw = url.split(":///", 1)[-1]
    Path(raw).expanduser().resolve().parent.mkdir(parents=True, exist_ok=True)


@lru_cache
def get_settings() -> Settings:
    settings = Settings()
    settings.data_dir.mkdir(parents=True, exist_ok=True)
    (settings.data_dir / "sources").mkdir(exist_ok=True)
    (settings.data_dir / "artifacts").mkdir(exist_ok=True)
    _ensure_sqlite_parent(settings.database_url)
    return settings
