from jarvis.nlu.normalization_words import (
    STOP_PHRASES,
    STOP_WORDS,
)


class EntityNormalizer:

    def normalize(self, entity: str) -> str:

        entity = entity.lower().strip()

        for phrase in STOP_PHRASES:
            entity = entity.replace(phrase, " ")

        words = entity.split()

        words = [
            word
            for word in words
            if word not in STOP_WORDS
        ]

        return " ".join(words).strip()
