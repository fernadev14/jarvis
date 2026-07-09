from enum import Enum


class TokenKind(str, Enum):

    UNKNOWN = "unknown"

    VERB = "verb"

    NOUN = "noun"

    ARTICLE = "article"

    PRONOUN = "pronoun"

    PREPOSITION = "preposition"

    AUXILIARY = "auxiliary"

    POLITENESS = "politeness"

    CONTEXT = "context"

    CONNECTOR = "connector"

    DESCRIPTOR = "descriptor"
