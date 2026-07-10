from jarvis.models.token_kind import TokenKind


class EntityExtractor:

    IGNORE = {
        "el",
        "la",
        "los",
        "las",
        "de",
        "del",
        "por",
        "favor",
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

            if word in self.IGNORE:
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
            # descriptor
            #

            if token.kind == TokenKind.DESCRIPTOR:
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
