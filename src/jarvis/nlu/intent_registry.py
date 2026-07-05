from jarvis.nlu.intent_patterns import (
    OPEN_PATTERNS,
    CHAT_PATTERNS,
)


class IntentRegistry:

    def get_patterns(self) -> dict[str, list[str]]:

        return {
            "open": OPEN_PATTERNS,
            "chat": CHAT_PATTERNS,
        }
