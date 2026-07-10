from jarvis.models.action_result import ActionResult
from jarvis.models.resource_type import ResourceType
from jarvis.platforms.factory import PlatformFactory
from jarvis.skills.base import Skill


class OpenSkill(Skill):

    def __init__(self):

        self.platform = PlatformFactory.create()

    @property
    def intent(self):

        return "open"

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
                resource.url,
                understanding.tool,
            )

        elif resource.resource_type == ResourceType.FOLDER:

            ok = self.platform.open_folder(
                resource.path
            )

        elif resource.resource_type == ResourceType.FILE:

            ok = self.platform.open_file(
                resource.path
            )

        else:

            return ActionResult(
                success=False,
                message=f"No puedo abrir recursos de tipo '{resource.resource_type.value}'.",
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
