from pathlib import Path

from studykit.config import Settings


class FileStore:
    def __init__(self, settings: Settings):
        self.root = settings.data_dir
        self.sources = self.root / "sources"
        self.artifacts = self.root / "artifacts"
        self.sources.mkdir(parents=True, exist_ok=True)
        self.artifacts.mkdir(parents=True, exist_ok=True)

    def write_source(self, kit_id: str, filename: str, data: bytes) -> Path:
        suffix = Path(filename).suffix.lower() or ".txt"
        path = self.sources / f"{kit_id}{suffix}"
        path.write_bytes(data)
        return path

    def read_source(self, path: str | Path) -> str:
        return Path(path).read_text(encoding="utf-8")

    def write_artifact(self, kit_id: str, html: str) -> Path:
        folder = self.artifacts / kit_id
        folder.mkdir(parents=True, exist_ok=True)
        path = folder / "index.html"
        path.write_text(html, encoding="utf-8")
        return path

    def artifact_path(self, kit_id: str) -> Path:
        return self.artifacts / kit_id / "index.html"
