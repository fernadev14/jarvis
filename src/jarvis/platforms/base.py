from abc import ABC, abstractmethod


class Platform(ABC):

    @abstractmethod
    def open_application(self, app: str) -> bool:
        pass

    @abstractmethod
    def shutdown(self) -> bool:
        pass

    @abstractmethod
    def restart(self) -> bool:
        pass
