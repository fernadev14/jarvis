from dataclasses import dataclass


@dataclass(slots=True)
class FileRecord:

    name: str

    path: str

    extension: str

    size: int

    modified: float

    is_directory: bool = False
