from jarvis.actions.open_application import OpenApplicationAction
from jarvis.actions.open_website import OpenWebsiteAction


class ActionRouter:

    def init(self):

        self.routes = {
            ("open", "application"): OpenApplicationAction(),
            ("open", "website"): OpenWebsiteAction(),
        }

    def route(self, understanding):

        key = (
            understanding.intent,
            understanding.entity_type.value,
        )

        return self.routes.get(key)
