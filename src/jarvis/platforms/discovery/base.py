from abc import ABC, abstractmethod


class DiscoveryRepository(ABC):

    @abstractmethod
    def load(self):
        ...
