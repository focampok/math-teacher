# Studykit

Open-source compiler that turns a Markdown or text syllabus into a **self-contained study kit**: practice (multiple choice and numeric), formula sheets, and a recitation page. The kit is a single HTML file. Students need a browser, not an account.

The first production example is **Matemática IV · admisión 2026**. That hand-built kit remains available; the platform can also render the same syllabus from a JSON schema.

This is a study aid. **It does not guarantee exam results.**

## How it works

The language model **never writes HTML**.

1. You upload `.md`, `.txt`, or a `KitSchema` `.json`.
2. A compiler (`StubCompiler` without an API key, or `OpenAICompatibleCompiler`) produces JSON.
3. Pydantic validates it: block weights must sum to 100, every block has items, answers are well-formed.
4. A Jinja renderer emits `index.html`.
5. You preview, then publish at `/k/{slug}`.

```
upload → Postgres job → compile → render → review → publish
                              ↘ failed (error on the job)
```

Locally you can skip Docker: SQLite + the stub compiler. Railway uses Postgres, a volume at `/data`, and one web service (the queue worker runs inside that process).

## Requirements

- Python 3.12+
- Optional: Docker, a Postgres instance, an OpenAI-compatible API key

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

The API also polls the job queue (no second process and no Redis). Set `RUN_EMBEDDED_WORKER=false` only if you start `python -m studykit.worker` yourself.

- Health: <http://127.0.0.1:8000/health>
- App: <http://127.0.0.1:8000/>
- Original Matemática IV kit: <http://127.0.0.1:8000/k/matematica-iv>
- Same syllabus through the renderer: <http://127.0.0.1:8000/k/matematica-iv/generated>

Upload (default token `change-me`, or whatever you put in `.env`):

```bash
curl -F file=@examples/matematica-iv/kit.schema.json \
  -H "X-Upload-Token: change-me" \
  http://127.0.0.1:8000/kits
```

`StubCompiler` accepts a raw `KitSchema` JSON file (or a fenced ` ```json ` block). Any other Markdown becomes a small demonstration kit so contributors can exercise the pipeline without paying for tokens.

## Docker Compose

```bash
docker compose up --build
```

Web is on port 8000. The embedded worker writes kits to the same `/data` volume.

## Deploy on Railway

1. Create a project from this repo (Dockerfile builder).
2. Add the **Postgres** plugin **before** the first successful boot. The app rewrites `postgres://` / `postgresql://` to `postgresql+psycopg://` automatically.
3. Add a **Volume** mounted at `/data` on the **web** service (Railway cannot share one volume across two services).
4. Web service start command (already in `railway.toml`):

   `sh -c 'alembic upgrade head && uvicorn studykit.api.main:app --host 0.0.0.0 --port $PORT'`

   Do not add a second worker service. The web process drains the Postgres queue itself.

5. Environment on web:

   | Variable | Notes |
   |---|---|
   | `DATABASE_URL` | From the plugin; prefix `postgresql+psycopg://` if needed |
   | `UPLOAD_TOKEN` | Shared secret for upload / publish |
   | `DATA_DIR` | `/data` |
   | `PUBLIC_BASE_URL` | `https://your-service.up.railway.app` |
   | `LLM_API_KEY` | Optional. Empty → stub |
   | `LLM_BASE_URL` | Default `https://api.openai.com/v1` |
   | `LLM_MODEL` | Default `gpt-4o-mini` |

Health check path: `/health`.

## Repository layout

```
studykit/           application (api, catalog, compiler, renderer, worker)
examples/matematica-iv/
  source/           original Markdown + HTML of the first kit
  kit.schema.json   golden schema for tests
  dist/index.html   hand-assembled fallback served at /k/matematica-iv
docs/adr/           architecture decisions
tests/
```

The historical `src/` tree is the same kit before the platform existed. Prefer `examples/matematica-iv/`.

## License

[MIT](LICENSE) © Francisco Ocampo

See [CONTRIBUTING.md](CONTRIBUTING.md) to run tests and add an LLM adapter.
