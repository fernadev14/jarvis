from jarvis.models.resource import Resource
from jarvis.models.resource_type import ResourceType


class ResourceFactory:

    def from_file(
        self,
        record,
    ):

        return Resource(
            id=f"file:{record.path}",
            name=record.name,
            resource_type=ResourceType.FILE,
            path=record.path,
        )
