from jarvis.search.filesystem.updaters.file_index_updater import (
    FileIndexUpdater,
)


class FilesystemUpdater:

    def __init__(self):

        self.index = FileIndexUpdater()

    def update(
        self,
        event,
    ):

        if event.event == "created":

            self.index.created(
                event.path,
            )

        elif event.event == "modified":

            self.index.modified(
                event.path,
            )

        elif event.event == "deleted":

            self.index.deleted(
                event.path,
            )
