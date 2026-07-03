from jarvis.actions.base import Action
from jarvis.knowledge.applications import ApplicationRegistry
from jarvis.models.action_result import ActionResult
from jarvis.platforms.factory import PlatformFactory


class OpenApplicationAction(Action):

    @property
    def intent(self):
        return "open"

    @property
    def entity_type(self):
        return "application"

    def __init__(self):

        self.registry = ApplicationRegistry()

        self.platform = PlatformFactory.create()

    def execute(self, understanding):

        app = self.registry.find(understanding.entity)

        if app is None:

            return ActionResult(
                success=False,
                message=f"No conozco la aplicación '{understanding.entity}'.",
            )

        ok = self.platform.open_application(app.executable)

        if ok:

            return ActionResult(
                success=True,
                message=f"He abierto {app.name}.",
            )

        return ActionResult(
            success=False,
            message=f"No pude abrir {app.name}.",
        )
