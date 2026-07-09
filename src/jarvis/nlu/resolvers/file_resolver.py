from jarvis.files.search_engine import SearchEngine
from jarvis.models.resource import Resource
from jarvis.models.resource_type import ResourceType


class FileResolver:

    def __init__(self):

        self.search_engine = SearchEngine()

    def resolve(self, entity: str) -> Resource | None:

        file = self.search_engine.search(entity)

        if file is None:
            return None

        return Resource(
            name=file.name,
            resource_type=ResourceType.FILE,
            path=str(file),
        )
