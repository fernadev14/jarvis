from jarvis.models.token import Token
from jarvis.models.token_kind import TokenKind

from jarvis.nlu.entity_extractor import EntityExtractor


extractor = EntityExtractor()


def token(word, index):

    return Token(
        text=word,
        normalized=word,
        index=index,
        kind=TokenKind.NOUN,
    )


tests = [

    (
        "abre firefox",

        [
            token("firefox", 0),
        ],
    ),

    (
        "abre github en firefox",

        [
            token("github", 0),
            token("en", 1),
            token("firefox", 2),
        ],
    ),

    (
        "abre contrato desde documentos",

        [
            token("contrato", 0),
            token("desde", 1),
            token("documentos", 2),
        ],
    ),

    (
        "abre google chrome",

        [
            token("google", 0),
            token("chrome", 1),
        ],
    ),

]

for sentence, tokens in tests:

    print("-" * 50)

    print(sentence)

    print(extractor.extract(tokens))
