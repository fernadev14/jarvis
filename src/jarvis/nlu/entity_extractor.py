from jarvis.models.intent_match import IntentMatch
from jarvis.models.token import Token


class EntityExtractor:

    def extract(
        self,
        tokens: list[Token],
        match: IntentMatch,
    ) -> str:

        if match.verb_index == -1:
            return ""

        entity = []

        for token in tokens:

            if token.index > match.verb_index:

                entity.append(token.text)

        return " ".join(entity)
