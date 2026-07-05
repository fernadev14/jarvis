from jarvis.files.search_engine import SearchEngine
from jarvis.knowledge.registry import KnowledgeRegistry
from jarvis.models.resource import Resource
from jarvis.models.resource_type import ResourceType


class EntityResolver:

    def __init__(self):

        self.registry = KnowledgeRegistry()
        self.search_engine = SearchEngine()

    def resolve(self, entity: str) -> Resource | None:

        # 1. Buscar recursos conocidos
        resource = self.registry.find(entity)

        if resource is not None:

            return Resource(
                name=resource.name,
                resource_type=ResourceType(resource.type),
                executable=resource.executable,
                url=resource.url,
                path=resource.path,
            )

        # 2. Buscar archivos
        file = self.search_engine.search(entity)

        if file is not None:

            return Resource(
                name=file.name,
                resource_type=ResourceType.FILE,
                path=str(file),
            )

        return None
