from abc import ABC, abstractmethod


class Platform(ABC):
    """
    Interfaz base para todas las plataformas.
    """

    @abstractmethod
    def open_application(self, executable: str) -> bool:
        """
        Abre una aplicación instalada.
        """
        raise NotImplementedError

    @abstractmethod
    def open_url(self, url: str) -> bool:
        """
        Abre una URL en el navegador predeterminado.
        """
        raise NotImplementedError
