from jarvis.search.factories.resource_factory import (
    ResourceFactory,
)

from jarvis.search.indexers.file_indexer import (
    FileIndexer,
)


class FilesystemIndexer:

    def __init__(self):

        self.resource_factory = ResourceFactory()

        self.file_indexer = FileIndexer()

    def index(
        self,
        record,
    ):

        resource = self.resource_factory.build(
            record,
        )

        item = self.file_indexer.index(
            resource,
        )

        return (
            resource,
            item,
        )
