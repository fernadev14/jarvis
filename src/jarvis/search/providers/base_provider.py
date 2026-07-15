from abc import ABC
from abc import abstractmethod


class SearchProvider(ABC):

    @abstractmethod
    def load(
        self,
        index,
        repository,
    ):
        """
        Construye el índice inicial.
        """
        pass

    def refresh(
        self,
        index,
        repository,
    ):
        """
        Actualiza únicamente este proveedor.

        Por defecto vuelve a cargar todo,
        pero luego cada Provider podrá hacerlo
        de forma incremental.
        """

        self.load(
            index,
            repository,
        )
