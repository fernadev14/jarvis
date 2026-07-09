class VerbNormalizer:

    SUFFIXES = [
        "melo",
        "mela",
        "melos",
        "melas",
        "melo",
        "mela",
        "melo",
        "me",
        "lo",
        "la",
        "los",
        "las",
    ]

    def normalize(self, word: str) -> str:

        word = word.lower()

        for suffix in sorted(self.SUFFIXES, key=len, reverse=True):

            if word.endswith(suffix):

                word = word[:-len(suffix)]

                break

        return word
