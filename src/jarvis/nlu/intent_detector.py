from jarvis.models.intent_match import IntentMatch
from jarvis.nlu.intent_registry import IntentRegistry


class IntentDetector:

    def __init__(self):

        self.registry = IntentRegistry()

    def detect(self, text: str) -> IntentMatch:

        text = text.lower().strip()

        patterns = self.registry.get_patterns()

        for intent, pattern_list in patterns.items():

            for pattern in pattern_list:

                if text.startswith(pattern):

                    return IntentMatch(
                        intent=intent,
                        pattern=pattern,
                        start=0,
                        end=len(pattern),
                    )

        return IntentMatch(
            intent="chat",
            pattern="",
            start=0,
            end=0,
        )
