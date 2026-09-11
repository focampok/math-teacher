import json

import httpx
import pytest

from studykit.compiler.llm import OpenAICompatibleCompiler, _parse_json
from studykit.compiler.stub import StubCompiler, fixture_schema
from studykit.config import Settings
from studykit.domain.schema import KitSchema


def test_stub_parses_json_source():
    schema = fixture_schema()
    out = StubCompiler().compile(schema.model_dump_json(), "kit.json")
    assert out.title == schema.title


def test_stub_fenced_json():
    schema = fixture_schema()
    source = "Notas\n\n```json\n" + json.dumps(schema.model_dump()) + "\n```\n"
    out = StubCompiler().compile(source, "notes.md")
    assert out.blocks[0].id == "b1"


def test_stub_fixture_without_json():
    out = StubCompiler().compile("# Historia de Roma\nLos cónsules…", "roma.md")
    assert out.title
    KitSchema.model_validate(out.model_dump())


def test_parse_json_rejects_array():
    with pytest.raises(ValueError):
        _parse_json("[1, 2]")


def test_llm_retries_then_fails(monkeypatch):
    settings = Settings(llm_api_key="sk-test", llm_timeout_seconds=1)
    compiler = OpenAICompatibleCompiler(settings)
    calls = {"n": 0}

    def boom(*_a, **_k):
        calls["n"] += 1
        raise httpx.HTTPError("down")

    monkeypatch.setattr(compiler, "_chat", boom)
    with pytest.raises(ValueError):
        compiler.compile("tema", "a.md")
    assert calls["n"] == 3


def test_llm_accepts_valid_payload(monkeypatch):
    settings = Settings(llm_api_key="sk-test")
    compiler = OpenAICompatibleCompiler(settings)
    payload = fixture_schema().model_dump()

    def fake_chat(*_a, **_k):
        return json.dumps(payload)

    monkeypatch.setattr(compiler, "_chat", fake_chat)
    out = compiler.compile("cualquier texto", "x.md")
    assert out.title == payload["title"]
