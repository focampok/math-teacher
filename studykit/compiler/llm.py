from __future__ import annotations

import json
import re
from typing import Any

import httpx
from pydantic import ValidationError

from studykit.compiler.stub import StubCompiler
from studykit.config import Settings
from studykit.domain.schema import KitSchema

_SYSTEM = """You convert study notes (Markdown or plain text) into ONE JSON object of this shape:

{
  "title": string,
  "kicker": string,
  "subtitle": string,
  "session_len": 8,
  "full_len": 20,
  "points_per_item": 5,
  "blocks": [
    {
      "id": "b1",
      "name": string,
      "weight": int,
      "topics": [string],
      "formulas": [{"label": string, "eq": string, "note": string}],
      "bank": [
        {
          "type": "mc" | "num",
          "cat": string,
          "prompt": string,
          "hint": string,
          "explain": string,
          "opts": [string],
          "correct": 0,
          "answer": 0,
          "tol": 0.01
        }
      ]
    }
  ],
  "express": [{"n": 1, "text": string, "hide": string}]
}

Rules:
- Reply with JSON only. No markdown fences.
- Block weights MUST sum to 100.
- Every block needs ≥1 topic and ≥2 bank items.
- mc items: 4 opts, correct is the 0-based index of the right option.
- num items: numeric answer you can justify from the source. Set opts/correct to null.
- Prefer extractive questions whose answer is in the notes. Do not invent numeric facts.
- For STEM, only write a number if the source states it or the arithmetic is trivial.
- express: 6–18 recitation lines; put the hidden fragment in "hide".
- Write in the same language as the source.
"""


class OpenAICompatibleCompiler:
    def __init__(self, settings: Settings):
        self.settings = settings
        self._fallback = StubCompiler()

    def compile(self, source: str, filename: str = "source.md") -> KitSchema:
        last_error = "LLM did not return a valid KitSchema"
        for attempt in range(3):
            try:
                raw = self._chat(source, filename, last_error if attempt else "")
                data = _parse_json(raw)
                return KitSchema.model_validate(data)
            except (ValidationError, ValueError, httpx.HTTPError) as exc:
                last_error = str(exc)
        raise ValueError(last_error)

    def _chat(self, source: str, filename: str, previous_error: str) -> str:
        user = f"Filename: {filename}\n\n---\n{source[:80_000]}"
        if previous_error:
            user += (
                "\n\nThe previous JSON failed validation. Fix it. Error:\n"
                + previous_error[:2000]
            )
        payload: dict[str, Any] = {
            "model": self.settings.llm_model,
            "temperature": 0.2,
            "messages": [
                {"role": "system", "content": _SYSTEM},
                {"role": "user", "content": user},
            ],
        }
        # Best-effort JSON mode; some compatible providers ignore it.
        payload["response_format"] = {"type": "json_object"}
        headers = {
            "Authorization": f"Bearer {self.settings.llm_api_key}",
            "Content-Type": "application/json",
        }
        url = self.settings.llm_base_url.rstrip("/") + "/chat/completions"
        with httpx.Client(timeout=self.settings.llm_timeout_seconds) as client:
            response = client.post(url, headers=headers, json=payload)
            response.raise_for_status()
            body = response.json()
        try:
            return body["choices"][0]["message"]["content"]
        except (KeyError, IndexError, TypeError) as exc:
            raise ValueError(f"unexpected LLM response: {body!r}") from exc


def _parse_json(text: str) -> dict:
    text = text.strip()
    fence = re.search(r"```(?:json)?\s*(\{.*\})\s*```", text, re.DOTALL)
    if fence:
        text = fence.group(1)
    try:
        data = json.loads(text)
    except json.JSONDecodeError as exc:
        raise ValueError(f"LLM output is not JSON: {exc}") from exc
    if not isinstance(data, dict):
        raise ValueError("LLM output must be a JSON object")
    return data


def build_compiler(settings: Settings):
    if settings.llm_api_key:
        return OpenAICompatibleCompiler(settings)
    return StubCompiler()
