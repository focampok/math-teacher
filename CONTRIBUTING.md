# Contributing

Thanks for looking at Studykit. The hosted demo at [math-teacher.focampo.com](https://math-teacher.focampo.com) is up for 30 days; everyday work happens on your laptop.

## Setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
cp .env.example .env
pytest -q
ruff check studykit tests
```

Do not commit `.env` or API keys. CI runs the same pytest suite against SQLite (`ruff` + `pytest` on Python 3.12).

## Architecture rules

- Compilers return a `KitSchema`. They must not emit HTML.
- The renderer is deterministic. If a kit looks wrong, fix the schema or the Jinja template, not a one-off HTML patch.
- New persistence goes through Alembic (`alembic revision --autogenerate` after changing `studykit/domain/models.py`).
- Tests must pass without `LLM_API_KEY`. Use `StubCompiler` or mock `_chat`.
- Authoring copy is Spanish. Learner kits stay a single HTML file.

## Good first changes

1. **Example kit** — add `examples/<slug>/kit.schema.json` that validates (`KitSchema`) and a short `README.md` in that folder. Prefer extractive items. Do not invent numeric answers the notes do not support.
2. **Compiler adapter** — implement `compile(self, source: str, filename: str) -> KitSchema` (see `studykit/compiler/base.py`). Raise `ValueError` with a readable message when the provider or the JSON fails validation. Wire it in `studykit/compiler/llm.py` `build_compiler`. Add a unit test that never hits the network.
3. **Tests** — a failing case around weights, item shapes, upload errors, or the renderer.

## Pull requests

1. Fork [focampok/math-teacher](https://github.com/focampok/math-teacher) and branch from `main`.
2. Keep the change small. One concern per PR.
3. `pytest -q` and `ruff check studykit tests` must pass.
4. Describe *why* in the PR body. Link an issue if there is one.

Issues are welcome: bugs, a kit you want to add, or a question about the 30-day demo.

## Running a worker locally

`uvicorn` starts the queue worker in-process. A second terminal is optional:

```bash
RUN_EMBEDDED_WORKER=false uvicorn studykit.api.main:app --reload
python -m studykit.worker
```

Both processes must share `DATABASE_URL` and `DATA_DIR`.
