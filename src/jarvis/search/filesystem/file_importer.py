from jarvis.search.filesystem.file_record_loader import (
    FileRecordLoader,
)

from jarvis.search.filesystem.filesystem_indexer import (
    FilesystemIndexer,
)


class FileImporter:

    def __init__(self):

        self.loader = FileRecordLoader()

        self.indexer = FilesystemIndexer()

    def load(
        self,
        path,
    ):

        record = self.loader.load(
            path,
        )

        if record is None:
            return None

        return self.load_record(
            record,
        )

    def load_record(
        self,
        record,
    ):

        return self.indexer.index(
            record,
        )
