from abc import ABC, abstractmethod


class Platform(ABC):

    @abstractmethod
    def open_application(self, executable: str) -> bool:
        ...

    @abstractmethod
    def open_url(
        self,
        url: str,
        browser: str = "",
    ) -> bool:
        ...

    @abstractmethod
    def open_folder(self, path: str) -> bool:
        ...

    @abstractmethod
    def open_file(self, path: str) -> bool:
        ...
