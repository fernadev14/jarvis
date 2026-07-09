from jarvis.models.sentence import Sentence
from jarvis.models.token import Token
from jarvis.nlu.lexicon import GREETING_WORDS, OPEN_VERBS


class SentenceParser:

    def parse(
        self,
        tokens: list[Token],
    ) -> Sentence:

        sentence = Sentence(tokens=tokens)

        # Buscar el verbo principal
        for token in tokens:

            if token.normalized in OPEN_VERBS:

                sentence.verb = token.normalized
                sentence.verb_index = token.index

                break

        # Si no encontró verbo
        if sentence.verb_index == -1:

            for token in tokens:

                if token.normalized in GREETING_WORDS:

                    sentence.verb = token.normalized
                    sentence.verb_index = token.index

                    break

        # Extraer el objeto (todo después del verbo)
        if sentence.verb_index != -1:

            words = []

            for token in tokens:

                if token.index > sentence.verb_index:

                    words.append(token.text)

            sentence.object = " ".join(words)

        return sentence
