from jarvis.knowledge.registry import KnowledgeRegistry
from jarvis.models.resource import Resource
from jarvis.models.resource_type import ResourceType


class KnowledgeResolver:

    def __init__(self):

        self.registry = KnowledgeRegistry()

    def resolve(self, entity: str) -> Resource | None:

        resource = self.registry.find(entity)

        if resource is None:
            return None

        return Resource(
            name=resource.name,
            resource_type=ResourceType(resource.type),
            executable=resource.executable,
            url=resource.url,
            path=resource.path,
        )
