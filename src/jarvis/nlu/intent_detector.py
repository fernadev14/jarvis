from jarvis.models.intent_match import IntentMatch
from jarvis.models.token import Token
from jarvis.nlu.lexicon import (
    GREETING_WORDS,
    OPEN_VERBS,
)


class IntentDetector:

    def detect(
        self,
        tokens: list[Token],
    ) -> IntentMatch:

        for token in tokens:

            if token.normalized in OPEN_VERBS:

                return IntentMatch(
                    intent="open",
                    verb=token.normalized,
                    verb_index=token.index,
                )

        for token in tokens:

            if token.normalized in GREETING_WORDS:

                return IntentMatch(
                    intent="chat",
                    verb=token.normalized,
                    verb_index=token.index,
                )

        return IntentMatch(
            intent="chat",
            verb="",
            verb_index=-1,
        )
