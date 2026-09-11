from functools import lru_cache
from pathlib import Path

from jinja2 import Environment, FileSystemLoader, select_autoescape

from studykit.domain.schema import KitSchema

_TEMPLATES = Path(__file__).resolve().parent / "templates"


@lru_cache
def _env() -> Environment:
    return Environment(
        loader=FileSystemLoader(_TEMPLATES),
        autoescape=select_autoescape(["html"]),
    )


def render_kit(schema: KitSchema, storage_key: str | None = None) -> str:
    """Deterministic HTML. Fails if the schema is invalid (already validated)."""
    payload = schema.model_dump()
    payload["full_plan"] = schema.full_plan()
    payload["storage_key"] = storage_key or _storage_key(schema)
    return _env().get_template("kit.html").render(kit=payload, schema=schema)


def _storage_key(schema: KitSchema) -> str:
    slug = "".join(ch if ch.isalnum() else "-" for ch in schema.title.lower()).strip("-")
    return f"studykit:{slug[:40] or 'kit'}"
