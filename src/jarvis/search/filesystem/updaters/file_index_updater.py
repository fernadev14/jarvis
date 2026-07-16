from jarvis.search.filesystem.file_importer import (
    FileImporter,
)


class FileIndexUpdater:

    def __init__(
        self,
        service,
    ):

        self.service = service

        self.importer = FileImporter()

    # Metodo privado para cargar un archivo y
    # devolver el resultado de la importación.
    # Si el archivo no se puede cargar, devuelve None.
    def _load(
        self,
        path,
    ):

        result = self.importer.load(
            path,
        )

        if result is None:
            return None

        return result

    def created(
        self,
        path,
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
        path,
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
        path,
    ):

        self.service.remove(
            f"file:{path}",
        )
