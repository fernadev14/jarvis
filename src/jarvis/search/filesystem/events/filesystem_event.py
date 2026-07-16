from dataclasses import dataclass
from pathlib import Path

from jarvis.search.filesystem.events.filesystem_event_type import (
    FilesystemEventType,
)


@dataclass(slots=True)
class FilesystemEvent:

    event: FilesystemEventType

    path: Path
