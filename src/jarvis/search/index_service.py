from jarvis.resources.repository import ResourceRepository
from jarvis.search.index import SearchIndex


class IndexService:

    def __init__(
        self,
        index: SearchIndex,
        repository: ResourceRepository,
    ):
        self.index = index
        self.repository = repository

    def add(
        self,
        resource,
        item,
    ):
        self.repository.add(resource)
        self.index.add(item)

    def remove(
        self,
        resource_id,
    ):

        self.repository.remove(
            resource_id,
        )

        self.index.remove(
            resource_id,
        )

    def replace(
        self,
        resource,
        item,
    ):

        self.repository.add(
            resource,
        )

        self.index.replace(
            item,
        )
