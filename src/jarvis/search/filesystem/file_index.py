from collections.abc import Iterator

from jarvis.search.filesystem.file_record import FileRecord


class FileIndex:

    def __init__(self):

        self.records: list[FileRecord] = []

    def add(
        self,
        record: FileRecord,
    ):

        self.records.append(record)

    def extend(
        self,
        records: list[FileRecord],
    ):

        self.records.extend(records)

    def all(self):

        return self.records

    def clear(self):

        self.records.clear()

    def __iter__(self) -> Iterator[FileRecord]:

        return iter(self.records)

    def __getitem__(
        self,
        index,
    ) -> FileRecord:

        return self.records[index]

    def __contains__(
        self,
        item,
    ):

        return item in self.records

    def __len__(self):

        return len(self.records)
