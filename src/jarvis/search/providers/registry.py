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

    def providers(self):

        return [

            KnowledgeProvider(),

            DesktopProvider(),

            FilesystemProvider(),

        ]
