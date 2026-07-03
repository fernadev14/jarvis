# DIRECTOR

from jarvis.core.brain import Brain


class Assistant:

    def __init__(self):
        self.brain = Brain()

    def chat(self, message: str) -> str:
        return self.brain.ask(message)
