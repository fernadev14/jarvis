from jarvis.platforms.userdirs.user_directories import (
    UserDirectories,
)

from jarvis.search.filesystem.filesystem_indexer import (
    FilesystemIndexer,
)

from jarvis.resources.repository import ResourceRepository

from jarvis.search.filesystem.scanner import FileScanner

from jarvis.search.index import SearchIndex

# from jarvis.search.indexers.file_indexer import (
#     FileIndexer,
# )

# from jarvis.search.factories.resource_factory import (
#     ResourceFactory,
# )


class FileLoader:

    def __init__(self):

        self.directories = UserDirectories()

        self.scanner = FileScanner()

        self.indexer = FilesystemIndexer()

        # self.indexer = FileIndexer()

        # self.factory = ResourceFactory()

    def load(
        self,
        index: SearchIndex,
        repository: ResourceRepository,
    ):

        files = self.scanner.index(
            self.directories.documents(),
        )

        for record in files.all():

            resource, item = self.indexer.index(
                record,
            )

            repository.add(
                resource,
            )

            index.add(
                item,
            )
