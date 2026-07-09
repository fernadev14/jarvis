from jarvis.nlu.resolvers.file_resolver import FileResolver
from jarvis.nlu.resolvers.knowledge_resolver import KnowledgeResolver


class EntityResolver:

    def __init__(self):

        self.resolvers = [
            KnowledgeResolver(),
            FileResolver(),
        ]

    def resolve(self, entity: str):

        for resolver in self.resolvers:

            resource = resolver.resolve(entity)

            if resource is not None:
                return resource

        return None
