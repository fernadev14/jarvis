from jarvis.resources.repository import ResourceRepository

from jarvis.search.index import SearchIndex
from jarvis.search.ranking import Ranking

from jarvis.search.loaders.knowledge_loader import (
    KnowledgeLoader,
)

from jarvis.search.loaders.desktop_loader import (
    DesktopLoader,
)


class SearchEngine:

    def __init__(self):

        self.ranking = Ranking()

        self.index = SearchIndex()

        self.repository = ResourceRepository()

        KnowledgeLoader().load(

            self.index,

            self.repository,
        )

        DesktopLoader().load(

            self.index,

            self.repository,
        )

    def search(
        self,
        query: str,
        context: str = "",
    ):

        return self.ranking.rank(
            query=query,
            items=self.index.all(),
            context=context,
        )

    def get_resource(self, resource_id):

        return self.repository.get(resource_id)

    def best(
        self,
        query: str,
        context: str = "",
    ):

        results = self.search(
            query,
            context,
        )

        if not results:
            return None

        return results[0]

    def resolve(
        self,
        query: str,
        context: str = "",
    ):
        result = self.best(
            query,
            context,
        )

        if result is None:
            return None

        return self.repository.get(
            result.item.resource_id
        )
