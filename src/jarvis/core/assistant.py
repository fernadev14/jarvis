from jarvis.core.action_manager import ActionManager
from jarvis.core.brain import Brain
from jarvis.core.intent import Intent
from jarvis.core.planner import Planner


class Assistant:

    def __init__(self):

        self.brain = Brain()

        self.planner = Planner()

        self.actions = ActionManager()

    def chat(self, message: str):

        request = self.planner.detect(message)

        if request.intent != Intent.CHAT:

            result = self.actions.execute(request)

            return result.message

        return self.brain.ask(message)
