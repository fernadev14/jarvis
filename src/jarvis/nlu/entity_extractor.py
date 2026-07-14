from jarvis.models.token_kind import TokenKind


class EntityExtractor:

    TOOL_CONNECTORS = {
        "en",
        "con",
    }

    LOCATION_CONNECTORS = {
        "desde",
        "en",
        "dentro",
        "de",
    }

    def extract(self, tokens):

        target = []

        tool = ""

        location = ""

        mode = "target"

        for token in tokens:

            word = token.normalized

            #
            # conectores
            #

            if word in self.TOOL_CONNECTORS:

                mode = "tool"
                continue

            if word in self.LOCATION_CONNECTORS:

                mode = "location"
                continue

            #
            # ignorar verbos y contexto
            #

            if token.kind == TokenKind.VERB:
                continue

            if token.kind == TokenKind.CONTEXT:
                continue

            #
            # target
            #

            if mode == "target":

                target.append(word)

            #
            # herramienta
            #

            elif mode == "tool":

                tool = word

            #
            # ubicación
            #

            elif mode == "location":

                location = word

        return {
            "target": " ".join(target),
            "tool": tool,
            "location": location,
        }
