from abc import ABC
from abc import abstractmethod


class SearchIndexer(ABC):

    @abstractmethod
    def index(
        self,
        source,
        resource,
    ):
        ...
