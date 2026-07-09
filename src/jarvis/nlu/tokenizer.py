from jarvis.models.token import Token


class Tokenizer:

    def tokenize(
        self,
        text: str,
    ) -> list[Token]:

        words = text.split()

        tokens = []

        for index, word in enumerate(words):

            tokens.append(
                Token(
                    text=word,
                    normalized=word.lower(),
                    index=index,
                )
            )

        return tokens
