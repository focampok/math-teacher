from __future__ import annotations

import json
import re
from pathlib import Path

from pydantic import ValidationError

from studykit.domain.schema import KitSchema

_JSON_FENCE = re.compile(r"```(?:json)?\s*(\{.*\})\s*```", re.DOTALL)


def _first_heading(source: str) -> str:
    for line in source.splitlines():
        stripped = line.strip().lstrip("#").strip()
        if stripped:
            return stripped[:120]
    return "Kit de estudio"


def fixture_schema(title: str | None = None) -> KitSchema:
    """Playable kit used when the source is not already JSON."""
    return KitSchema.model_validate(
        {
            "title": title or "Kit de demostración",
            "kicker": "Studykit",
            "subtitle": "Generado por StubCompiler (sin API key).",
            "blocks": [
                {
                    "id": "b1",
                    "name": "Conceptos",
                    "weight": 60,
                    "topics": ["Definiciones", "Lectura activa"],
                    "formulas": [
                        {"label": "Idea clave", "eq": "leer → practicar → recitar", "note": ""}
                    ],
                    "bank": [
                        {
                            "type": "mc",
                            "cat": "Lectura",
                            "prompt": "¿Qué produce Studykit a partir de un Markdown?",
                            "opts": [
                                "Un kit HTML autocontenido",
                                "Un PDF firmado",
                                "Una cuenta de alumno",
                                "Un LMS completo",
                            ],
                            "correct": 0,
                            "hint": "El renderer escribe un solo index.html.",
                            "explain": "El LLM (o el stub) escribe JSON; el renderer lo vuelve un kit estático.",
                        },
                        {
                            "type": "mc",
                            "cat": "Arquitectura",
                            "prompt": "¿Quién escribe el HTML del kit?",
                            "opts": [
                                "El modelo de lenguaje",
                                "El renderer determinista",
                                "El navegador del alumno",
                                "Netlify Functions",
                            ],
                            "correct": 1,
                            "hint": "El contrato es KitSchema, no HTML libre.",
                            "explain": "El compiler solo emite JSON validado. Jinja arma el HTML.",
                        },
                    ],
                },
                {
                    "id": "b2",
                    "name": "Práctica",
                    "weight": 40,
                    "topics": ["Preguntas numéricas", "Repaso"],
                    "formulas": [{"label": "Peso", "eq": "bloques = 100", "note": "Suma de pesos."}],
                    "bank": [
                        {
                            "type": "num",
                            "cat": "Pesos",
                            "prompt": "Si los bloques deben sumar 100 y uno vale 60, ¿cuánto vale el otro?",
                            "answer": 40,
                            "tol": 0.01,
                            "hint": "100 − 60.",
                            "explain": "100 − 60 = 40.",
                        },
                        {
                            "type": "num",
                            "cat": "Simulacro",
                            "prompt": "Cada acierto del simulacro vale 5 puntos. ¿Cuántas preguntas hacen 100?",
                            "answer": 20,
                            "tol": 0.01,
                            "hint": "100 ÷ 5.",
                            "explain": "100 / 5 = 20 preguntas.",
                        },
                    ],
                },
            ],
            "express": [
                {"n": 1, "text": "El compiler escribe JSON, no HTML.", "hide": "JSON"},
                {"n": 2, "text": "Los pesos de los bloques suman 100.", "hide": "100"},
            ],
        }
    )


class StubCompiler:
    """Parse JSON sources; otherwise return a playable fixture (no API key)."""

    def compile(self, source: str, filename: str = "source.md") -> KitSchema:
        text = source.strip()
        parsed = _try_json(text)
        if parsed is not None:
            try:
                return KitSchema.model_validate(parsed)
            except ValidationError as exc:
                raise ValueError(f"source looks like JSON but is not a valid KitSchema: {exc}") from exc
        title = _first_heading(text)
        if filename:
            stem = Path(filename).stem.replace("_", " ").strip()
            if stem and stem.lower() not in {"source", "upload"}:
                title = stem[:120]
        return fixture_schema(title)


def _try_json(text: str) -> dict | None:
    if text.startswith("{"):
        try:
            data = json.loads(text)
            return data if isinstance(data, dict) else None
        except json.JSONDecodeError:
            return None
    fence = _JSON_FENCE.search(text)
    if fence:
        try:
            data = json.loads(fence.group(1))
            return data if isinstance(data, dict) else None
        except json.JSONDecodeError:
            return None
    return None
