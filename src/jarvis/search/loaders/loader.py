from abc import ABC
from abc import abstractmethod


class Loader(ABC):

    @abstractmethod
    def load(
        self,
        index,
        repository,
    ):
        ...
