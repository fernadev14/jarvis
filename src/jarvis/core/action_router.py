from jarvis.actions.open_application import OpenApplicationAction
from jarvis.actions.open_website import OpenWebsiteAction
from jarvis.nlu.understanding import Understanding


class ActionRouter:

    def __init__(self):

        self.routes = {}

        self.register(OpenApplicationAction())
        self.register(OpenWebsiteAction())

    def register(self, action):

        key = (
            action.intent,
            action.entity_type,
        )

        self.routes[key] = action

    def route(self, understanding: Understanding):

        key = (
            understanding.intent,
            understanding.entity_type.value,
        )

        return self.routes.get(key)
