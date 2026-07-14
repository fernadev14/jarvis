from abc import ABC
from abc import abstractmethod


class Scorer(ABC):

    @abstractmethod
    def score(
        self,
        query,
        candidate,
    ) -> float:
        pass
