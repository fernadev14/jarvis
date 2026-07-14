from jarvis.search.providers.desktop_provider import (
    DesktopProvider,
)

from jarvis.search.providers.filesystem_provider import (
    FilesystemProvider,
)

from jarvis.search.providers.knowledge_provider import (
    KnowledgeProvider,
)


class ProviderRegistry:

    def __init__(self):

        self._providers = []

    def register(
        self,
        provider,
    ):

        self._providers.append(provider)

    def providers(self):

        return self._providers
