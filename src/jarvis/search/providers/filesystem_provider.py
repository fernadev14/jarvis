from jarvis.search.loaders.file_loader import FileLoader

from jarvis.search.providers.base_provider import (
    SearchProvider,
)


class FilesystemProvider(SearchProvider):

    def __init__(self):

        self.loader = FileLoader()

    def load(
        self,
        service,
    ):

        self.loader.load(
            service,
        )
