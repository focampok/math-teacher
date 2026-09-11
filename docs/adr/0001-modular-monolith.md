# ADR 0001 — Modular monolith, not microservices

**Status:** Accepted  
**Date:** 2026-09-11

## Context

Studykit has one maintainer, an evolving domain, and ~0.1 QPS of generation jobs. The write path (upload → compile → render) and the read path (serve a static kit) share one schema and one volume.

## Decision

Ship a single FastAPI process plus a worker process from the **same image**. Module boundaries (`api`, `catalog`, `compiler`, `renderer`, `storage`) live in one package.

## Consequences

- One deploy, one on-call, one database.
- The worker and web fail together and are debugged together — intentional.
- If a second team appears, extract the worker first; do not start with a service mesh.
