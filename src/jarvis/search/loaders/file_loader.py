from jarvis.platforms.userdirs.user_directories import (
    UserDirectories,
)

from jarvis.search.filesystem.filesystem_indexer import (
    FilesystemIndexer,
)

from jarvis.resources.repository import ResourceRepository

from jarvis.search.filesystem.scanner import FileScanner

from jarvis.search.index import SearchIndex


class FileLoader:

    def __init__(self):

        self.directories = UserDirectories()

        self.scanner = FileScanner()

        self.indexer = FilesystemIndexer()

    def load(
        self,
        service,
    ):

        files = self.scanner.index(
            self.directories.documents(),
        )

        for record in files.all():

            resource, item = self.indexer.index(
                record,
            )

            service.add(
                resource,
                item,
            )
