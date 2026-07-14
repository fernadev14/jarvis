from jarvis.resources.repository import ResourceRepository

from jarvis.search.index import SearchIndex

from jarvis.search.loaders.file_loader import FileLoader


class FilesystemProvider:

    def __init__(self):

        self.loader = FileLoader()

    def load(
        self,
        index: SearchIndex,
        repository: ResourceRepository,
    ):

        self.loader.load(
            index=index,
            repository=repository,
        )
