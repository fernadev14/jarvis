from jarvis.intent.command import (
    Command,
)

from jarvis.intent.intent_result import (
    IntentResult,
)


class OpenCommand(Command):

    prefix = "abre"

    def __init__(
        self,
        search,
        launcher,
    ):

        self.search = search

        self.launcher = launcher

    def execute(
        self,
        text,
    ):

        query = self.argument(
            text,
        )

        resource = self.search.resolve(
            query,
        )

        if resource is None:

            return IntentResult(
                success=False,
                message="No encontré el recurso.",
            )

        self.launcher.open(
            resource,
        )

        return IntentResult(
            success=True,
            message=f"Abriendo {resource.name}",
            resource=resource,
        )
