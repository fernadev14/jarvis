from jarvis.knowledge.registry import KnowledgeRegistry

from jarvis.models.resource import Resource
from jarvis.models.resource_type import ResourceType

from jarvis.resources.repository import ResourceRepository


from jarvis.search.index import SearchIndex

from jarvis.search.indexers.knowledge_indexer import (
    KnowledgeIndexer,
)
# from jarvis.search.item import SearchItem


class KnowledgeLoader:

    def __init__(self):

        self.registry = KnowledgeRegistry()
        self.indexer = KnowledgeIndexer()

    def load(
        self,
        index: SearchIndex,
        repository: ResourceRepository,
    ):

        for item in self.registry.resources.values():

            resource = Resource(

                id=f"knowledge:{item.name}",

                name=item.name,

                resource_type=ResourceType(item.type),

                executable=item.executable,

                url=item.url,

                path=item.path,
            )

            repository.add(resource)

            index.add(
                self.indexer.index(
                    resource,
                    item.aliases,
                )
            )
