from functools import lru_cache
from pathlib import Path

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


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
    max_upload_bytes: int = 1_000_000
    upload_rate_per_hour: int = 10

    example_slug: str = Field(default="matematica-iv")


@lru_cache
def get_settings() -> Settings:
    settings = Settings()
    settings.data_dir.mkdir(parents=True, exist_ok=True)
    (settings.data_dir / "sources").mkdir(exist_ok=True)
    (settings.data_dir / "artifacts").mkdir(exist_ok=True)
    return settings
