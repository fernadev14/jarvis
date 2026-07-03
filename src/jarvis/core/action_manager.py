from jarvis.actions.open_application import OpenApplicationAction
from jarvis.actions.registry import ActionRegistry


class ActionManager:

    def __init__(self):

        self.registry = ActionRegistry()

        self.registry.register(
            OpenApplicationAction()
        )

    def execute(self, request):

        action = self.registry.get(request.intent)

        if action is None:

            return None

        return action.execute(request)
