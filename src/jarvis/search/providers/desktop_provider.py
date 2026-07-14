from jarvis.search.loaders.desktop_loader import (
    DesktopLoader,
)

from jarvis.search.providers.provider import (
    SearchProvider,
)


class DesktopProvider(SearchProvider):

    def __init__(self):

        self.loader = DesktopLoader()

    def load(
        self,
        index,
        repository,
    ):

        self.loader.load(
            index,
            repository,
        )
