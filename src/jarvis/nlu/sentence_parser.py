from jarvis.models.sentence import Sentence
from jarvis.models.token_kind import TokenKind


IGNORED_NOUNS = {
    "aplicacion",
    "archivo",
    "carpeta",
    "navegador",
}


class SentenceParser:

    def parse(self, tokens):

        verb = ""
        target = ""
        context = ""
        tool = ""
        location = ""

        #
        # Buscar verbo
        #
        for token in tokens:

            if token.kind == TokenKind.VERB:

                verb = token.normalized
                break

        #
        # Buscar contexto
        #
        for token in tokens:

            if token.kind == TokenKind.CONTEXT:

                context = token.normalized
                break

        #
        # Buscar herramienta
        #
        for i, token in enumerate(tokens):

            if token.normalized in {
                "en",
                "con",
            }:

                if i + 1 < len(tokens):

                    tool = tokens[i + 1].normalized

        #
        # Buscar ubicación
        #
        for i, token in enumerate(tokens):

            if token.normalized == "desde":

                if i + 1 < len(tokens):

                    location = tokens[i + 1].normalized

        #
        # Buscar recurso
        #
        for token in tokens:

            if token.kind != TokenKind.NOUN:
                continue

            if token.normalized in IGNORED_NOUNS:
                continue

            target = token.normalized
            break

        return Sentence(

            intent="open",

            verb=verb,

            target=target,

            context=context,

            tool=tool,

            location=location,

            modifiers=[],
        )
