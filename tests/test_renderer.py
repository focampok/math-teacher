import json
from pathlib import Path

from studykit.compiler.stub import fixture_schema
from studykit.domain.schema import KitSchema
from studykit.renderer.engine import render_kit

ROOT = Path(__file__).resolve().parents[1]


def test_golden_matematica_has_four_views_and_shuffle():
    raw = json.loads((ROOT / "examples/matematica-iv/kit.schema.json").read_text(encoding="utf-8"))
    schema = KitSchema.model_validate(raw)
    html = render_kit(schema, storage_key="studykit:test")
    assert 'id="view-inicio"' in html
    assert 'id="view-practica"' in html
    assert 'id="view-formulas"' in html
    assert 'id="view-expres"' in html
    assert "function shuffle" in html
    assert "KIT_DATA" in html
    assert "Geometría y Trigonometría" in html
    assert "Factorización" in html
    for block in schema.blocks:
        assert f'id="f-{block.id}"' in html
    assert '"type": "mc"' in html or '"type":"mc"' in html
    assert "full_plan" in html


def test_n_blocks_not_hardcoded_to_five():
    html = render_kit(fixture_schema())
    assert "Conceptos" in html
    assert "Práctica" in html
    assert 'id="f-b1"' in html
    assert 'id="f-b2"' in html
    assert 'id="f-b5"' not in html


def test_example_fallback_exists():
    dist = ROOT / "examples/matematica-iv/dist/index.html"
    assert dist.is_file()
    text = dist.read_text(encoding="utf-8")
    assert "Matemática IV" in text
