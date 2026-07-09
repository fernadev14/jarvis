from jarvis.models.token_kind import TokenKind


class ContextExtractor:

    def extract(self, tokens):

        context = ""
        browser = ""

        for index, token in enumerate(tokens):

            if token.kind == TokenKind.CONTEXT:
                context = token.normalized

            if token.normalized == "en":

                if index + 1 < len(tokens):

                    browser = tokens[index + 1].normalized

        return {
            "context": context,
            "browser": browser,
        }
