from pathlib import Path

from jarvis.search.filesystem.file_importer import (
    FileImporter,
)


class FilesystemIndexService:

    def __init__(
        self,
        service,
    ):

        self.service = service

        self.importer = FileImporter()

    def _load(
        self,
        path: Path,
    ):

        return self.importer.load(
            path,
        )

    def created(
        self,
        path: Path,
    ):

        result = self._load(
            path,
        )

        if result is None:
            return

        resource, item = result

        self.service.add(
            resource,
            item,
        )

    def modified(
        self,
        path: Path,
    ):

        result = self._load(
            path,
        )

        if result is None:
            return

        resource, item = result

        self.service.replace(
            resource,
            item,
        )

    def deleted(
        self,
        path: Path,
    ):

        self.service.remove(
            f"file:{path}",
        )
