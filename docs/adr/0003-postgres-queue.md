# ADR 0003 — Job queue in Postgres

**Status:** Accepted  
**Date:** 2026-09-11

## Context

Generation is async (30 s–3 min) and rare. Redis/Celery would add a moving part without changing capacity.

## Decision

Jobs live in the same Postgres database. The worker claims a row with `FOR UPDATE SKIP LOCKED` and a `locked_until` lease. SQLite is used in tests and the local default; claiming falls back to a simple `UPDATE` of the oldest queued row.

## Consequences

- Railway needs only the Postgres plugin plus a volume.
- Revisit Redis if concurrent jobs exceed what one worker can drain.
