from jarvis.knowledge.registry import KnowledgeRegistry

from jarvis.models.resource import Resource
from jarvis.models.resource_type import ResourceType

from jarvis.search.indexers.knowledge_indexer import (
    KnowledgeIndexer,
)


class KnowledgeLoader:

    def __init__(self):

        self.registry = KnowledgeRegistry()
        self.indexer = KnowledgeIndexer()

    def load(
        self,
        service,
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

            search_item = self.indexer.index(
                item,
                resource,
            )

            service.add(
                resource,
                search_item,
            )
