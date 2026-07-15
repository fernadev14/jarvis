from jarvis.search.loaders.knowledge_loader import (
    KnowledgeLoader,
)

from jarvis.search.providers.base_provider import (
    SearchProvider,
)


class KnowledgeProvider(SearchProvider):

    def __init__(self):

        self.loader = KnowledgeLoader()

    def load(
        self,
        index,
        repository,
    ):

        self.loader.load(
            index,
            repository,
        )
