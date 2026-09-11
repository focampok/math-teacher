# Product

<!-- impeccable:product-schema 1 -->

## Platform

web

## Users

**Authors** — Francisco Ocampo and other teachers or collaborators who share `UPLOAD_TOKEN`. They arrive with a syllabus (Markdown, text, or `KitSchema` JSON) and need to publish a practice kit without writing HTML.

**Learners** — anyone with the public link. They study any subject in a browser. No account. The first shipped kits are Matemática IV (university admission) and Python for beginners; the product is not limited to those subjects.

## Product Purpose

Studykit turns a syllabus into a **self-contained study kit**: multiple-choice and numeric practice, formula sheets, and a recitation page. The kit is one HTML file. Success is a published `/k/{slug}` that a learner can open and use offline-in-the-tab, without installing an app.

This is a study aid. It does not guarantee exam results.

## Positioning

The language model **never writes HTML**. A compiler emits validated `KitSchema` JSON; a Jinja renderer emits `index.html`. Neighboring “AI website” tools that generate markup directly cannot claim this split. Authors who already have a schema skip the model entirely.

## Operating Context

- Authoring happens in the FastAPI admin (Spanish): upload → queue → compile → render → preview → publish.
- Production is one Railway web service, Postgres, and a volume at `/data`. The queue worker runs inside that process.
- Local default is SQLite plus `uvicorn studykit.api.main:app --reload`.
- Learners only use `/k/{slug}`. They must not see the token, the upload form, or admin chrome.
- Write access is a shared secret (`UPLOAD_TOKEN`), not per-user accounts.

## Capabilities and Constraints

- Open source, MIT, © Francisco Ocampo.
- Package `studykit` in the `math-teacher` repo.
- Compilers must return `KitSchema`. Block weights must sum to 100. The renderer is deterministic.
- Without `LLM_API_KEY`, Markdown/TXT becomes a demonstration kit; exact questions require JSON.
- v1 does not include student accounts, Redis, or object storage.
- Undecided: replacing the shared token with per-author accounts; formal WCAG target.

## Brand Commitments

- Product name: **Studykit**.
- Owner site: [focampo.com](https://focampo.com).
- Authoring voice: Spanish, direct, names the next action. No exam promises.
- Student kits stay self-contained HTML; they are the artifact, not a web app shell.

## Evidence on Hand

- `examples/matematica-iv/` — original admission kit (source, golden schema, hand-built `dist/index.html` at `/k/matematica-iv`).
- `examples/python-15/` — Python-for-beginners schema and notes.
- Do not invent testimonials, rankings, or outcome claims.

## Product Principles

1. The schema is the source of truth; fix content or the template, not a one-off HTML patch.
2. A published kit must work as a single file in a browser.
3. Authoring is a short pipeline (subir → generar → revisar → publicar), not a CMS.
4. Learners never cross into the authoring surface.
5. Honesty over persuasion: reinforcement tool, not a guarantee.

## Accessibility & Inclusion

Authoring already uses Spanish copy, a skip link, and large touch targets. No formal accessibility standard was committed. Learner kits must remain usable on a phone without an account.
