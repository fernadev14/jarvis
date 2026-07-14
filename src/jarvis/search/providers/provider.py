from abc import ABC
from abc import abstractmethod


class SearchProvider(ABC):

    @abstractmethod
    def load(
        self,
        index,
        repository,
    ):
        pass
