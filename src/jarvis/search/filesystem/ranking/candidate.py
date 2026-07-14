from dataclasses import dataclass

from jarvis.search.filesystem.file_record import FileRecord


@dataclass(slots=True)
class FileCandidate:

    record: FileRecord

    score: float
