from jarvis.resources.repository import ResourceRepository

from jarvis.search.index import SearchIndex

from jarvis.search.providers.desktop_provider import (
    DesktopProvider,
)

from jarvis.search.providers.knowledge_provider import (
    KnowledgeProvider,
)

from jarvis.search.providers.registry import (
    ProviderRegistry,
)


class SearchIndexBuilder:

    def build(self):

        index = SearchIndex()

        repository = ResourceRepository()

        providers = ProviderRegistry().providers()

        for provider in providers:

            provider.load(
                index,
                repository,
            )

        return (
            index,
            repository,
        )
