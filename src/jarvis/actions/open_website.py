from jarvis.actions.base import Action
from jarvis.models.action_result import ActionResult
from jarvis.models.entity_type import EntityType
from jarvis.platforms.factory import PlatformFactory


class OpenWebsiteAction(Action):

    def __init__(self):

        self.platform = PlatformFactory.create()

    @property
    def intent(self):
        return "open"

    @property
    def entity_type(self):
        return EntityType.WEBSITE

    def execute(self, understanding):

        entity = understanding.resolved

        if entity is None:

            return ActionResult(
                success=False,
                message="No conozco ese sitio web.",
            )

        ok = self.platform.open_url(entity.url)

        if ok:

            return ActionResult(
                success=True,
                message=f"Abriendo {entity.name}.",
            )

        return ActionResult(
            success=False,
            message=f"No pude abrir {entity.name}.",
        )
