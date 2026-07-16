from jarvis.resources.repository import ResourceRepository

from jarvis.search.index import SearchIndex
from jarvis.search.index_service import IndexService

from jarvis.search.lifecycle.lifecycle_manager import (
    LifecycleManager,
)

from jarvis.search.providers.desktop_provider import (
    DesktopProvider,
)

from jarvis.search.providers.filesystem_provider import (
    FilesystemProvider,
)

from jarvis.search.providers.knowledge_provider import (
    KnowledgeProvider,
)

from jarvis.search.providers.registry import (
    ProviderRegistry,
)
from jarvis.search.search_context import SearchContext


class SearchIndexBuilder:

    def build(self):

        index = SearchIndex()

        repository = ResourceRepository()

        service = IndexService(
            index=index,
            repository=repository,
        )

        registry = ProviderRegistry()

        registry.register(KnowledgeProvider())
        registry.register(DesktopProvider())
        registry.register(FilesystemProvider())

        lifecycle = LifecycleManager()

        lifecycle.load(
            registry.providers(),
            service,
        )

        return SearchContext(
            index=index,
            repository=repository,
            service=service,
        )
