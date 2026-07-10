class SearchTokenizer:

    STOP_WORDS = {

        "de",
        "del",
        "la",
        "las",
        "los",
        "el",

        "y",

        "en",

        "por",

        "favor",

        "con",

        "para",
    }

    def tokenize(self, text: str):

        return [

            word

            for word in text.split()

            if word not in self.STOP_WORDS
        ]
