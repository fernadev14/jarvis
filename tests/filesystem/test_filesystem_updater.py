from pathlib import Path

from jarvis.search.filesystem.events.filesystem_event import (
    FilesystemEvent,
)

from jarvis.search.filesystem.updaters.filesystem_updater import (
    FilesystemUpdater,
)

updater = FilesystemUpdater()

events = [

    FilesystemEvent(
        event="created",
        path=Path("/tmp/contrato.pdf"),
    ),

    FilesystemEvent(
        event="modified",
        path=Path("/tmp/cv.pdf"),
    ),

    FilesystemEvent(
        event="deleted",
        path=Path("/tmp/foto.jpg"),
    ),

]

for event in events:

    updater.update(
        event,
    )
