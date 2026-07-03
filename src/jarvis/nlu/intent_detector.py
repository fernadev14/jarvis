class IntentDetector:

    def detect(self, text: str):

        text = text.lower()

        if text.startswith("abre "):
            return "open"

        return "chat"
