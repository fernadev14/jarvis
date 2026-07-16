from abc import ABC
from abc import abstractmethod


class Command(ABC):

    prefix = ""

    def matches(
        self,
        text: str,
    ):

        return text.lower().startswith(
            f"{self.prefix} ",
        )

    def argument(
        self,
        text: str,
    ):

        return text.removeprefix(
            f"{self.prefix} ",
        ).strip()

    @abstractmethod
    def execute(
        self,
        text: str,
    ):

        pass
