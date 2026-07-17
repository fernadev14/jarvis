from abc import ABC
from abc import abstractmethod


class Command(ABC):

    prefixes = []

    def matches(
        self,
        text: str,
    ):

        text = text.lower().strip()

        for prefix in self.prefixes:

            if text.startswith(
                prefix + " ",
            ):
                return True

        return False

    def argument(
        self,
        text: str,
    ):

        text = text.strip()

        lower = text.lower()

        for prefix in self.prefixes:

            if lower.startswith(
                prefix + " ",
            ):

                return text[
                    len(prefix):
                ].strip()

        return text

    @abstractmethod
    def execute(
        self,
        text: str,
    ):

        pass
