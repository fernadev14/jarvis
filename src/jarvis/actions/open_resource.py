from pathlib import Path
from jarvis.actions.base import Action
from jarvis.models.action_result import ActionResult
from jarvis.models.resource_type import ResourceType
from jarvis.platforms.factory import PlatformFactory


class OpenResourceAction(Action):

    def __init__(self):

        self.platform = PlatformFactory.create()

    @property
    def intent(self):
        return "open"

    @property
    def entity_type(self):
        return None

    def execute(self, understanding):

        resource = understanding.resource

        if resource is None:

            return ActionResult(
                success=False,
                message="No conozco ese recurso.",
            )

        if resource.resource_type == ResourceType.APPLICATION:

            ok = self.platform.open_application(
                resource.executable
            )

        elif resource.resource_type == ResourceType.WEBSITE:

            ok = self.platform.open_url(
                resource.url
            )

        elif resource.resource_type == ResourceType.FOLDER:
            path = Path(resource.path).expanduser()
            ok = self.platform.open_folder(
                str(path)
            )

        elif resource.resource_type == ResourceType.FILE:
            ok = self.platform.open_file(
                resource.path
            )

        else:
            return ActionResult(
                success=False,
                message=f"Todavía no puedo abrir recursos de tipo '{resource.resource_type.value}'.",
            )

        if ok:

            return ActionResult(
                success=True,
                message=f"He abierto {resource.name}.",
            )

        return ActionResult(
            success=False,
            message=f"No pude abrir {resource.name}.",
        )
