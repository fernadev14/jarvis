from jarvis.platforms.userdirs.user_directories import UserDirectories
from jarvis.search.filesystem.filesystem_index_service import FilesystemIndexService
from jarvis.search.filesystem.watchers.file_watcher import FileWatcher


class FilesystemRuntime:

    def __init__(
        self,
        service,
    ):

        directories = UserDirectories()

        updater = FilesystemIndexService(
            service,
        )

        self.watcher = FileWatcher(
            directory=directories.documents(),
            updater=updater,
        )

    def start(self):

        self.watcher.start()

    def stop(self):

        self.watcher.stop()
