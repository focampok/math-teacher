import json
from pathlib import Path

import pytest
from pydantic import ValidationError

from studykit.domain.schema import KitSchema

ROOT = Path(__file__).resolve().parents[1]


def test_matematica_schema_validates():
    raw = json.loads((ROOT / "examples/matematica-iv/kit.schema.json").read_text(encoding="utf-8"))
    schema = KitSchema.model_validate(raw)
    assert sum(b.weight for b in schema.blocks) == 100
    assert len(schema.blocks) == 5
    plan = schema.full_plan()
    assert sum(p["count"] for p in plan) <= 20
    assert all(p["count"] >= 1 for p in plan)


def test_weights_must_sum_100():
    with pytest.raises(ValidationError):
        KitSchema.model_validate(
            {
                "title": "x",
                "kicker": "y",
                "blocks": [
                    {
                        "id": "b1",
                        "name": "A",
                        "weight": 50,
                        "topics": ["t"],
                        "bank": [
                            {
                                "type": "num",
                                "prompt": "p",
                                "hint": "h",
                                "explain": "e",
                                "answer": 1,
                            }
                        ],
                    }
                ],
            }
        )


def test_mc_needs_correct_index():
    with pytest.raises(ValidationError):
        KitSchema.model_validate(
            {
                "title": "x",
                "kicker": "y",
                "blocks": [
                    {
                        "id": "b1",
                        "name": "A",
                        "weight": 100,
                        "topics": ["t"],
                        "bank": [
                            {
                                "type": "mc",
                                "prompt": "p",
                                "hint": "h",
                                "explain": "e",
                                "opts": ["a", "b"],
                                "correct": 4,
                            }
                        ],
                    }
                ],
            }
        )
