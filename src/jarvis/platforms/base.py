from abc import ABC, abstractmethod


class Platform(ABC):

    @abstractmethod
    def open_application(self, executable: str) -> bool:
        pass

    @abstractmethod
    def open_url(self, url: str) -> bool:
        pass

    @abstractmethod
    def open_folder(self, path: str) -> bool:
        pass

    @abstractmethod
    def open_file(self, path: str) -> bool:
        pass
