from jarvis.search.loaders.desktop_loader import (
    DesktopLoader,
)

from jarvis.search.providers.base_provider import (
    SearchProvider,
)


class DesktopProvider(SearchProvider):

    def __init__(self):

        self.loader = DesktopLoader()

    def load(
        self,
        service,
    ):

        self.loader.load(
            service,
        )
