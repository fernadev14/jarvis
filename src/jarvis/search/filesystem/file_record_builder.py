from pathlib import Path

from jarvis.search.filesystem.file_record import (
    FileRecord,
)


class FileRecordBuilder:

    def build(
        self,
        path,
    ):

        file = Path(path)

        stat = file.stat()

        return FileRecord(

            name=file.stem,

            path=str(file),

            extension=file.suffix.lower(),

            size=stat.st_size,

            modified=stat.st_mtime,

            is_directory=file.is_dir(),
        )
