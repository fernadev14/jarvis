from jarvis.core.action_router import ActionRouter
from jarvis.core.brain import Brain
from jarvis.nlu.language_understanding import LanguageUnderstanding


class Assistant:

    def __init__(self):

        self.brain = Brain()

        self.nlu = LanguageUnderstanding()

        self.router = ActionRouter()

    def chat(self, message: str):

        understanding = self.nlu.understand(message)

        action = self.router.route(understanding)

        if action:

            result = action.execute(understanding)

            return result.message

        return self.brain.ask(message)
