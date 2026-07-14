class QueryCleaner:

    STOP_WORDS = {
        "el",
        "la",
        "los",
        "las",
        "un",
        "una",
        "por",
        "favor",
        "puedes",
        "podrias",
        "podrías",
        "quisiera",
        "quiero",
        "me",
    }

    RESOURCE_WORDS = {
        "archivo",
        "documento",
        "carpeta",
    }

    DESCRIPTORS = {
        "llama",
        "llamado",
        "llamada",
        "esta",
        "está",
        "dentro",
        "ubicado",
        "ubicada",
    }

    def clean(self, tokens):

        cleaned = []

        for token in tokens:

            word = token.normalized

            if word in self.STOP_WORDS:
                continue

            if word in self.RESOURCE_WORDS:
                continue

            if word in self.DESCRIPTORS:
                continue

            cleaned.append(token)

        return cleaned
