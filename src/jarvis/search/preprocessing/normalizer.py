import re
import unicodedata


class SearchNormalizer:

    def normalize(self, text: str) -> str:

        text = text.lower()

        text = unicodedata.normalize(
            "NFKD",
            text,
        )

        text = "".join(

            c

            for c in text

            if not unicodedata.combining(c)
        )

        text = re.sub(

            r"[^a-z0-9+ ]",

            " ",

            text,
        )

        text = re.sub(

            r"\s+",

            " ",

            text,
        )

        return text.strip()
