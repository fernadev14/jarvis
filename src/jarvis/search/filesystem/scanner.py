from pathlib import Path

from jarvis.search.filesystem.file_record import FileRecord
from jarvis.search.filesystem.ignore import IgnoreRules
from jarvis.search.filesystem.file_index import FileIndex
from jarvis.search.filesystem.filters.file_filter import FileFilter


class FileScanner:

    def __init__(self):

        self.ignore = IgnoreRules()
        self.file_filter = FileFilter()

    def scan(self, root):

        root = Path(root).expanduser().resolve()

        records = []

        self._scan_directory(
            root,
            records,
        )

        return records

    def index(
        self,
        directory,
    ):

        index = FileIndex()

        records = self.scan(directory)

        index.extend(records)

        return index

    def _scan_directory(
        self,
        directory,
        records,
    ):

        if not directory.exists():
            return

        try:

            for entry in directory.iterdir():

                if entry.is_dir():

                    if self.ignore.ignore(entry):
                        continue

                    self._scan_directory(
                        entry,
                        records,
                    )

                    continue

                if not self.file_filter.allow(entry):
                    continue

                stat = entry.stat()

                records.append(

                    FileRecord(

                        name=entry.stem,

                        path=str(entry),

                        extension=entry.suffix.lower(),

                        size=stat.st_size,

                        modified=stat.st_mtime,

                        is_directory=False,
                    )

                )

        except PermissionError:
            pass

        except FileNotFoundError:
            pass
