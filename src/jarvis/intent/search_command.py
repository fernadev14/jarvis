from jarvis.intent.command import (
    Command,
)

from jarvis.intent.intent_result import (
    IntentResult,
)


class SearchCommand(Command):

    prefix = "busca"

    def __init__(
        self,
        search,
    ):

        self.search = search

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

        return IntentResult(
            success=True,
            message=f"Encontré {resource.name}",
            resource=resource,
        )
