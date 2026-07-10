from jarvis.models.token_kind import TokenKind


class EntityExtractor:

    STOP_WORDS = {
        "el",
        "la",
        "los",
        "las",
        "de",
        "del",
        "por",
        "favor",
        "puedes",
        "podrias",
        "quisiera",
        "quiero",
        "me",
        "abre",
        "abrir",
        "abreme",
        "abrime",
    }

    TOOL_WORDS = {
        "en",
        "con",
    }

    TOOL_CONNECTORS = {
        "en",
        "con",
    }

    LOCATION_CONNECTORS = {
        "desde",
    }

    def extract(self, tokens):

        target = []

        tool = ""

        location = ""

        mode = "target"

        for token in tokens:

            word = token.normalized

            if word in self.STOP_WORDS:
                continue

            #
            # cambiar de modo
            #

            if word in self.TOOL_CONNECTORS:

                mode = "tool"
                continue

            if word in self.LOCATION_CONNECTORS:

                mode = "location"
                continue

            #
            # ignorar verbos
            #

            if token.kind == TokenKind.VERB:
                continue

            #
            # contexto
            #

            if token.kind == TokenKind.CONTEXT:
                continue

            #
            # target
            #

            if mode == "target":

                target.append(word)

            #
            # navegador
            #

            elif mode == "tool":

                if token.kind == TokenKind.NOUN:

                    tool = word

            #
            # ubicación
            #

            elif mode == "location":

                if token.kind == TokenKind.NOUN:

                    location = word

        return {
            "target": " ".join(target),
            "tool": tool,
            "location": location,
        }
