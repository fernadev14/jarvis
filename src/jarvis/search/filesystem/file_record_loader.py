from pathlib import Path

from jarvis.search.filesystem.file_record import (
    FileRecord,
)


class FileRecordLoader:

    def load(
        self,
        path,
    ):

        path = Path(path)

        if not path.exists():

            return None

        stat = path.stat()

        return FileRecord(

            name=path.stem,

            path=str(path),

            extension=path.suffix.lower(),

            size=stat.st_size,

            modified=stat.st_mtime,

            is_directory=path.is_dir(),
        )
