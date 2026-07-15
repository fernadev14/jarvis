from jarvis.models.resource import Resource


class ResourceRepository:

    def __init__(self):

        self.resources: dict[str, Resource] = {}

    def add(
        self,
        resource: Resource,
    ):

        self.resources[resource.id] = resource

    def remove(
        self,
        resource_id: str,
    ):

        self.resources.pop(
            resource_id,
            None,
        )

    def contains(
        self,
        resource_id: str,
    ):

        return resource_id in self.resources

    def get(
        self,
        resource_id: str,
    ):

        return self.resources.get(resource_id)

    def all(self):

        return list(
            self.resources.values(),
        )
