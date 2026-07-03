class EntityExtractor:

    def extract(self, text: str):

        text = text.lower().strip()

        if text.startswith("abre "):
            return text.replace("abre", "", 1).strip()

        return ""
