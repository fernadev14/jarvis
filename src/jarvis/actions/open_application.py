from jarvis.actions.base import Action
from jarvis.core.intent import Intent
from jarvis.knowledge.applications import ApplicationRegistry
from jarvis.models.action_request import ActionRequest
from jarvis.models.action_result import ActionResult
from jarvis.platforms.factory import PlatformFactory


class OpenApplicationAction(Action):

    def __init__(self):

        self.registry = ApplicationRegistry()

        self.platform = PlatformFactory.create()

    @property
    def intent(self) -> Intent:
        return Intent.OPEN_APP

    def execute(self, request: ActionRequest):

        app = self.registry.find(request.entity)

        if app is None:

            return ActionResult(
                success=False,
                message=f"No conozco la aplicación '{request.entity}'.",
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
