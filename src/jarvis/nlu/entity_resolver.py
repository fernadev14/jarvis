from jarvis.knowledge.registry import KnowledgeRegistry
from jarvis.models.resource import Resource
from jarvis.models.resource_type import ResourceType


class EntityResolver:

    def __init__(self):

        self.registry = KnowledgeRegistry()

    def resolve(self, entity: str) -> Resource | None:

        resource = self.registry.find(entity)

        if resource is None:
            return None

        resource_type = ResourceType(resource.type)

        return Resource(
            name=resource.name,
            resource_type=resource_type,
            executable=resource.executable,
            url=resource.url,
            path=resource.path,
        )
