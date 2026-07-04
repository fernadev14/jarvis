from jarvis.actions.open_resource import OpenResourceAction
from jarvis.nlu.understanding import Understanding


class ActionRouter:

    def __init__(self):

        self.actions = {
            "open": OpenResourceAction(),
        }

    def route(self, understanding: Understanding):

        return self.actions.get(
            understanding.intent
        )
