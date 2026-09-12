# Studykit

[![CI](https://github.com/focampok/math-teacher/actions/workflows/ci.yml/badge.svg)](https://github.com/focampok/math-teacher/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python 3.12+](https://img.shields.io/badge/python-3.12%2B-3776AB.svg)](https://www.python.org/downloads/)

Open-source compiler that turns a Markdown, text, or JSON syllabus into a **self-contained study kit**: practice (multiple choice and numeric), formula sheets, and a recitation page. The kit is one HTML file. Learners need a browser, not an account.

The language model **never writes HTML**. A compiler emits a validated `KitSchema`; Jinja renders `index.html`. If you already have the JSON, you can skip the model.

This is a study aid. **It does not guarantee exam results.**

## Try the 30-day demo

A hosted instance is up at **[math-teacher.focampo.com](https://math-teacher.focampo.com)** for **30 days** so you can click through the real product before cloning.

| Page | URL |
|---|---|
| Authoring (upload → publish) | [math-teacher.focampo.com](https://math-teacher.focampo.com/) |
| Matemática IV | [ /k/matematica-iv](https://math-teacher.focampo.com/k/matematica-iv) |
| Python for beginners | [ /k/python-15](https://math-teacher.focampo.com/k/python-15) |

The demo is a preview, not a production SLA. After those 30 days, run it locally or deploy your own copy (MIT). Do not treat published demo kits as permanent.

Authoring writes need `UPLOAD_TOKEN`. Ask in an issue if you want to try a publish on the demo; or use the public kits above with no token.

## Why contribute

The repo is public and MIT. One FastAPI process, SQLite on your laptop, no Redis, no paid API key for the first green test.

Useful first pull requests:

- a new `examples/<slug>/kit.schema.json` (any subject)
- a compiler adapter that returns `KitSchema` and never hits the network in tests
- a failing test around validation, the renderer, or the authoring flow

See [CONTRIBUTING.md](CONTRIBUTING.md).

## Requirements

- Python 3.12+
- Optional: Docker, Postgres, an OpenAI-compatible API key

## Quick start (no API key)

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
cp .env.example .env
mkdir -p data
pytest -q
uvicorn studykit.api.main:app --reload
```

The API also polls the job queue. Set `RUN_EMBEDDED_WORKER=false` only if you start `python -m studykit.worker` yourself.

- Health: <http://127.0.0.1:8000/health>
- App: <http://127.0.0.1:8000/>
- Matemática IV: <http://127.0.0.1:8000/k/matematica-iv>
- Python example: <http://127.0.0.1:8000/k/python-15>
- Same mates syllabus through the renderer: <http://127.0.0.1:8000/k/matematica-iv/generated>

Upload (default token `change-me`):

```bash
curl -F file=@examples/python-15/kit.schema.json \
  -H "X-Upload-Token: change-me" \
  http://127.0.0.1:8000/kits
```

`StubCompiler` accepts a raw `KitSchema` JSON file (or a fenced ` ```json ` block). Any other Markdown becomes a small demonstration kit so you can exercise the pipeline without paying for tokens.

## How it works

1. Upload `.md`, `.txt`, or a `KitSchema` `.json`.
2. `StubCompiler` (no key) or `OpenAICompatibleCompiler` produces JSON.
3. Pydantic validates it: block weights must sum to 100, every block has items, answers are well-formed.
4. The renderer emits `index.html`.
5. You preview, then publish at `/k/{slug}`.

```
upload → Postgres job → compile → render → review → publish
                              ↘ failed (error on the job)
```

Local default: SQLite. Production: Postgres, a volume at `/data`, one web service (the worker runs inside that process).

## Docker Compose

```bash
docker compose up --build
```

Web is on port 8000. The embedded worker writes kits to the same `/data` volume.

## Deploy on Railway

1. Create a project from this repo (Dockerfile builder).
2. Add the **Postgres** plugin before the first successful boot. The app rewrites `postgres://` / `postgresql://` to `postgresql+psycopg://`.
3. Add a **Volume** mounted at `/data` on the **web** service (Railway cannot share one volume across two services).
4. Start command (already in `railway.toml`):

   `sh -c 'alembic upgrade head && uvicorn studykit.api.main:app --host 0.0.0.0 --port $PORT'`

   Do not add a second worker service.

5. Environment on web:

   | Variable | Notes |
   |---|---|
   | `DATABASE_URL` | From the plugin |
   | `UPLOAD_TOKEN` | Shared secret for upload / publish |
   | `DATA_DIR` | `/data` |
   | `PUBLIC_BASE_URL` | `https://math-teacher.focampo.com` (or your origin) |
   | `LLM_API_KEY` | Optional. Empty → stub |
   | `LLM_BASE_URL` | Default `https://api.openai.com/v1` |
   | `LLM_MODEL` | Default `gpt-4o-mini` |

Health check path: `/health`. Custom domain is configured in Railway → Networking.

## Repository layout

```
studykit/                 application (api, catalog, compiler, renderer, worker)
examples/matematica-iv/   first kit (source, golden schema, hand-built dist)
examples/python-15/       Python-for-beginners schema
docs/adr/                 architecture decisions
tests/
```

The historical `src/` tree is the same Matemática IV kit from before the platform. Prefer `examples/matematica-iv/`.

## License

[MIT](LICENSE) © [Francisco Ocampo](https://focampo.com)

You may use, fork, and host your own copy. Contributions are under the same license.
