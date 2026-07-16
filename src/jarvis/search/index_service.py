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
