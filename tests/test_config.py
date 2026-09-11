from studykit.config import Settings, normalize_database_url


def test_normalize_railway_postgres_url():
    assert normalize_database_url("postgres://u:p@host:5432/db") == (
        "postgresql+psycopg://u:p@host:5432/db"
    )
    assert normalize_database_url("postgresql://u:p@host/db") == (
        "postgresql+psycopg://u:p@host/db"
    )
    assert normalize_database_url("postgresql+psycopg://u:p@host/db") == (
        "postgresql+psycopg://u:p@host/db"
    )
    assert normalize_database_url("sqlite:///./data/x.sqlite").startswith("sqlite:")


def test_embedded_worker_defaults_on():
    assert Settings(run_embedded_worker=True).run_embedded_worker is True
    assert Settings(run_embedded_worker=False).run_embedded_worker is False
