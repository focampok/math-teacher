import os
from pathlib import Path

import pytest
from fastapi.testclient import TestClient

os.environ.setdefault("DATABASE_URL", "sqlite:///./data/test.sqlite")
os.environ.setdefault("UPLOAD_TOKEN", "test-token")
os.environ.setdefault("DATA_DIR", "./data")
os.environ.setdefault("LLM_API_KEY", "")

from studykit.config import get_settings
from studykit.db import init_db, reset_engine


@pytest.fixture
def client(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> TestClient:
    db_path = tmp_path / "test.sqlite"
    data_dir = tmp_path / "data"
    data_dir.mkdir()
    monkeypatch.setenv("DATABASE_URL", f"sqlite:///{db_path}")
    monkeypatch.setenv("DATA_DIR", str(data_dir))
    monkeypatch.setenv("UPLOAD_TOKEN", "test-token")
    get_settings.cache_clear()
    reset_engine()
    init_db()
    from studykit.api.main import create_app

    with TestClient(create_app()) as test_client:
        yield test_client
    get_settings.cache_clear()
    reset_engine()
