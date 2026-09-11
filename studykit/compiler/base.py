from typing import Protocol

from studykit.domain.schema import KitSchema


class Compiler(Protocol):
    def compile(self, source: str, filename: str = "source.md") -> KitSchema:
        """Turn uploaded Markdown/text into a validated KitSchema."""
