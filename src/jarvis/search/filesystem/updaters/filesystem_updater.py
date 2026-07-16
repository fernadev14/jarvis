from jarvis.search.filesystem.updaters.file_index_updater import (
    FileIndexUpdater,
)

from jarvis.search.filesystem.events.filesystem_event_type import (
    FilesystemEventType,
)


class FilesystemUpdater:

    def __init__(
        self,
        service,
    ):

        self.index = FileIndexUpdater(
            service,
        )

    def update(
        self,
        event,
    ):

        if event.event == FilesystemEventType.CREATED:

            self.index.created(
                event.path,
            )

        elif event.event == FilesystemEventType.MODIFIED:

            self.index.modified(
                event.path,
            )

        elif event.event == FilesystemEventType.DELETED:

            self.index.deleted(
                event.path,
            )
