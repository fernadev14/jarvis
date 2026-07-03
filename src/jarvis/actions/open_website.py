from jarvis.actions.base import Action
from jarvis.knowledge.websites import WebsiteRegistry
from jarvis.models.action_result import ActionResult
from jarvis.nlu.understanding import EntityType
from jarvis.platforms.factory import PlatformFactory


class OpenWebsiteAction(Action):

    def __init__(self):

        self.registry = WebsiteRegistry()

        self.platform = PlatformFactory.create()

    @property
    def intent(self):
        return "open"

    @property
    def entity_type(self):
        return EntityType.WEBSITE

    def execute(self, understanding):

        site = self.registry.find(understanding.entity)

        if site is None:

            return ActionResult(
                success=False,
                message=f"No conozco el sitio '{understanding.entity}'.",
            )

        ok = self.platform.open_url(site["url"])

        if ok:

            return ActionResult(
                success=True,
                message=f"Abriendo {understanding.entity}.",
            )

        return ActionResult(
            success=False,
            message="No pude abrir el navegador.",
        )
