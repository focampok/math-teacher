# ADR 0002 — LLM writes KitSchema, never HTML

**Status:** Accepted  
**Date:** 2026-09-11

## Context

The Matemática IV kit is a hand-crafted HTML engine (practice, formulas, recitation). Letting a model emit HTML would make kits irreproducible and untestable.

## Decision

The compiler (stub or OpenAI-compatible) returns a `KitSchema` JSON document. A deterministic Jinja renderer produces the self-contained `index.html`. Validation lives on the Pydantic model: weights sum to 100, every block has items, MC/num answers are well-formed.

## Consequences

- Contributors run the stub with no API key.
- Review is a JSON diff, not a 200 KB HTML diff.
- STEM quality still needs human review; the schema does not invent a proof.
