from jarvis.resources.repository import ResourceRepository

from jarvis.search.index import SearchIndex

from jarvis.search.loaders.desktop_loader import (
    DesktopLoader,
)

from jarvis.search.loaders.knowledge_loader import (
    KnowledgeLoader,
)


class SearchIndexBuilder:

    def build(self):

        index = SearchIndex()

        repository = ResourceRepository()

        #
        # Cargar conocimiento
        #

        KnowledgeLoader().load(
            index,
            repository,
        )

        #
        # Cargar aplicaciones
        #

        DesktopLoader().load(
            index,
            repository,
        )

        return (
            index,
            repository,
        )
