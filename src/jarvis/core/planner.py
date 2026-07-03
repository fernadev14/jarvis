from jarvis.core.intent import Intent
from jarvis.models.action_request import ActionRequest


class Planner:

    def detect(self, message: str) -> ActionRequest:

        text = message.lower().strip()

        if text.startswith("abre "):

            entity = text.replace("abre", "", 1).strip()

            return ActionRequest(
                intent=Intent.OPEN_APP,
                text=message,
                entity=entity,
            )

        return ActionRequest(
            intent=Intent.CHAT,
            text=message,
            entity="",
        )
