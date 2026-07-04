from jarvis.files.finder import FileFinder
from jarvis.knowledge.registry import KnowledgeRegistry
from jarvis.models.resource import Resource
from jarvis.models.resource_type import ResourceType


class EntityResolver:

    def __init__(self):

        self.registry = KnowledgeRegistry()

        self.files = FileFinder()

    def resolve(self, entity: str) -> Resource | None:

        # -----------------------------
        # Buscar recurso conocido
        # -----------------------------

        resource = self.registry.find(entity)

        if resource is not None:

            return Resource(
                name=resource.name,
                resource_type=ResourceType(resource.type),
                executable=resource.executable,
                url=resource.url,
                path=resource.path,
            )

        # -----------------------------
        # Buscar archivo
        # -----------------------------

        file = self.files.find(entity)

        if file is not None:

            return Resource(
                name=file.name,
                resource_type=ResourceType.FILE,
                path=str(file),
            )

        return None
