from dataclasses import dataclass

from pathlib import Path


@dataclass(slots=True)
class FilesystemEvent:

    event: str

    path: Path
