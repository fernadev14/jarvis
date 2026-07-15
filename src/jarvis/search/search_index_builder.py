from jarvis.search.providers.desktop_provider import (
    DesktopProvider,
)

from jarvis.search.providers.filesystem_provider import (
    FilesystemProvider,
)

from jarvis.search.providers.knowledge_provider import (
    KnowledgeProvider,
)

from jarvis.resources.repository import ResourceRepository

from jarvis.search.index import SearchIndex

from jarvis.search.providers.registry import (
    ProviderRegistry,
)

from jarvis.search.lifecycle.lifecycle_manager import (
    LifecycleManager,
)


class SearchIndexBuilder:

    def build(self):

        index = SearchIndex()

        repository = ResourceRepository()

        registry = ProviderRegistry()

        registry.register(
            KnowledgeProvider(),
        )

        registry.register(
            DesktopProvider(),
        )

        registry.register(
            FilesystemProvider(),
        )

        lifecycle = LifecycleManager()

        for provider in registry.providers():

            lifecycle.register(
                provider,
            )

        lifecycle.load(
            index,
            repository,
        )

        return (
            index,
            repository,
        )
