from jarvis.actions.base import Action
from jarvis.models.action_result import ActionResult
from jarvis.knowledge.websites import WebsiteRegistry
import webbrowser


class OpenWebsiteAction(Action):

    @property
    def intent(self):
        return "open"

    @property
    def entity_type(self):
        return "website"

    def execute(self, understanding):
        registry = WebsiteRegistry()
        site = registry.find(understanding.entity)
        if site is None:
            return ActionResult(
                success=False,
                message="No conozco ese sitio web.",
            )

        webbrowser.open(site["url"])
        return ActionResult(
            success=True,
            message=f"Abriendo {understanding.entity}.",

        )
