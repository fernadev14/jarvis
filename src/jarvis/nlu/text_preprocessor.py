import re
import unicodedata


class TextPreprocessor:

    def preprocess(self, text: str) -> str:

        text = text.lower().strip()

        text = unicodedata.normalize(
            "NFD",
            text,
        )

        text = "".join(
            c
            for c in text
            if unicodedata.category(c) != "Mn"
        )

        text = re.sub(
            r"[^\w\s]",
            " ",
            text,
        )

        text = re.sub(
            r"\s+",
            " ",
            text,
        )

        return text.strip()
