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
        service,
    ):

        self.loader.load(
            service,
        )
