import unicodedata

from jarvis.nlp.verb_normalizer import (
    VerbNormalizer,
)


class TextNormalizer:

    def __init__(
        self,
    ):

        self.verbs = VerbNormalizer()

    def normalize(
        self,
        text: str,
    ):

        text = self._strip(
            text,
        )

        text = self._lower(
            text,
        )

        text = self._remove_accents(
            text,
        )

        text = self._collapse_spaces(
            text,
        )

        text = self.verbs.normalize(
            text,
        )

        return text

    def _strip(
        self,
        text,
    ):

        return text.strip()

    def _lower(
        self,
        text,
    ):

        return text.lower()

    def _remove_accents(
        self,
        text,
    ):

        normalized = unicodedata.normalize(
            "NFD",
            text,
        )

        return "".join(

            c

            for c in normalized

            if unicodedata.category(
                c,
            ) != "Mn"
        )

    def _collapse_spaces(
        self,
        text,
    ):

        return " ".join(
            text.split(),
        )
