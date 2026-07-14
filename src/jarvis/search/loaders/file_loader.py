from jarvis.models.resource import Resource
from jarvis.models.resource_type import ResourceType

from jarvis.platforms.userdirs.user_directories import (
    UserDirectories,
)

from jarvis.resources.repository import ResourceRepository

from jarvis.search.filesystem.scanner import FileScanner

from jarvis.search.index import SearchIndex

from jarvis.search.indexers.file_indexer import (
    FileIndexer,
)


class FileLoader:

    def __init__(self):

        self.directories = UserDirectories()

        self.scanner = FileScanner()

        self.indexer = FileIndexer()

    def load(
        self,
        index: SearchIndex,
        repository: ResourceRepository,
    ):

        files = self.scanner.index(
            self.directories.documents(),
        )

        for record in files.all():

            resource = Resource(

                id=f"file:{record.path}",

                name=record.name,

                resource_type=ResourceType.FILE,

                path=record.path,
            )

            repository.add(resource)

            item = self.indexer.index(
                resource,
            )

            index.add(item)
