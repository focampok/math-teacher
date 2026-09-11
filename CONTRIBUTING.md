# Contributing

## Setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
cp .env.example .env
pytest -q
ruff check studykit tests
```

Do not commit `.env` or API keys. CI runs the same pytest suite against SQLite.

## Architecture rules

- Compilers return a `KitSchema`. They must not emit HTML.
- The renderer is deterministic. If a kit looks wrong, fix the schema or the Jinja template, not a one-off HTML patch.
- New persistence goes through Alembic (`alembic revision --autogenerate` after changing `studykit/domain/models.py`).
- Tests must pass without `LLM_API_KEY`. Use `StubCompiler` or mock `_chat`.

## Adding an LLM adapter

1. Implement `compile(self, source: str, filename: str) -> KitSchema` (see `studykit/compiler/base.py`).
2. Raise `ValueError` with a readable message when the provider or the JSON fails validation. The worker stores that string on the job.
3. Wire it in `studykit/compiler/llm.py` `build_compiler`.
4. Add a unit test that never hits the network.

STEM sources: prefer extractive items. Do not invent numeric answers the notes do not support.

## Running a worker locally

`uvicorn` starts the queue worker in-process. A second terminal is optional:

```bash
RUN_EMBEDDED_WORKER=false uvicorn studykit.api.main:app --reload
python -m studykit.worker
```

Both processes must share `DATABASE_URL` and `DATA_DIR`.
