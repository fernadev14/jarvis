from pathlib import Path

from jarvis.resources.repository import ResourceRepository

from jarvis.search.filesystem.events.filesystem_event import (
    FilesystemEvent,
)

from jarvis.search.filesystem.updaters.filesystem_updater import (
    FilesystemUpdater,
)

from jarvis.search.index import SearchIndex
from jarvis.search.index_service import IndexService


index = SearchIndex()

repository = ResourceRepository()

service = IndexService(
    index=index,
    repository=repository,
)

updater = FilesystemUpdater(
    service,
)

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
