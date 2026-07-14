from jarvis.search.rewriter.stopwords import (
    STOPWORDS,
)

from jarvis.search.rewriter.synonyms import (
    SYNONYMS,
)


class RewriteRules:

    def apply(
        self,
        text: str,
    ):

        text = text.lower()

        #
        # sinónimos
        #

        for old, new in SYNONYMS.items():

            text = text.replace(
                old,
                new,
            )

        #
        # stopwords
        #

        words = []

        for word in text.split():

            if word in STOPWORDS:

                continue

            words.append(word)

        return " ".join(words)
