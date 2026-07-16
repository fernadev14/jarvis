from jarvis.intent.command_registry import (
    CommandRegistry,
)

from jarvis.intent.open_command import (
    OpenCommand,
)

from jarvis.intent.search_command import (
    SearchCommand,
)

from jarvis.resources.launcher import (
    ResourceLauncher,
)


class IntentEngine:

    def __init__(
        self,
    ):

        from jarvis.search.search import (
            SearchEngine,
        )

        self.search = SearchEngine()

        self.launcher = ResourceLauncher()

        self.registry = CommandRegistry()

        self.registry.register(
            OpenCommand(
                self.search,
                self.launcher,
            )
        )

        self.registry.register(
            SearchCommand(
                self.search,
            )
        )

    def execute(
        self,
        text,
    ):

        text = text.strip()

        for command in self.registry.commands():

            if command.matches(
                text,
            ):

                return command.execute(
                    text,
                )

        return None

    def stop(
        self,
    ):

        self.search.stop()
