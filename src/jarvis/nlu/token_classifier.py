from jarvis.models.token import Token
from jarvis.models.token_kind import TokenKind
from jarvis.nlu.lexicon import (
    OPEN_VERBS,
    AUXILIARIES,
    CONTEXT_WORDS,
    CONNECTOR_WORDS,
    DESCRIPTOR_WORDS,
)
from jarvis.nlu.verb_normalizer import VerbNormalizer


ARTICLES = {
    "el",
    "la",
    "los",
    "las",
    "un",
    "una",
    "unos",
    "unas",
}

PRONOUNS = {
    "me",
    "te",
    "se",
    "lo",
    "la",
    "los",
    "las",
}

PREPOSITIONS = {
    "de",
    "del",
    "a",
    "con",
    "para",
    "por",
}

AUXILIARIES = {
    "puedes",
    "podrias",
    "quiero",
    "necesito",
    "ayudame",
    "ayudas",
}

POLITENESS = {
    "favor",
}


class TokenClassifier:

    def __init__(self):
        self.verb_normalizer = VerbNormalizer()

    def classify(
        self,
        tokens: list[Token],
    ) -> list[Token]:

        for token in tokens:

            word = self.verb_normalizer.normalize(
                token.normalized,
            )

            if word in OPEN_VERBS:
                token.kind = TokenKind.VERB

            elif token.normalized in ARTICLES:
                token.kind = TokenKind.ARTICLE

            elif token.normalized in PRONOUNS:
                token.kind = TokenKind.PRONOUN

            elif token.normalized in PREPOSITIONS:
                token.kind = TokenKind.PREPOSITION

            elif token.normalized in AUXILIARIES:
                token.kind = TokenKind.AUXILIARY

            elif token.normalized in CONTEXT_WORDS:
                token.kind = TokenKind.CONTEXT

            elif token.normalized in CONNECTOR_WORDS:
                token.kind = TokenKind.CONNECTOR

            elif token.normalized in DESCRIPTOR_WORDS:
                token.kind = TokenKind.DESCRIPTOR

            elif token.normalized in POLITENESS:
                token.kind = TokenKind.POLITENESS

            else:
                token.kind = TokenKind.NOUN

        return tokens
