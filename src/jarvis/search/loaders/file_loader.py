from jarvis.platforms.userdirs.user_directories import (
    UserDirectories,
)

from jarvis.search.filesystem.scanner import FileScanner

from jarvis.search.filesystem.file_importer import (
    FileImporter,
)


class FileLoader:

    def __init__(self):

        self.directories = UserDirectories()

        self.scanner = FileScanner()

        self.importer = FileImporter()

    def load(
        self,
        service,
    ):

        files = self.scanner.index(
            self.directories.documents(),
        )

        for record in files.all():

            result = self.importer.load_record(
                record,
            )

            if result is None:
                continue

            resource, item = result

            service.add(
                resource,
                item,
            )
