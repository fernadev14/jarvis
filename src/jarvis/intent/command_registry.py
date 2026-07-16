class CommandRegistry:

    def __init__(self):

        self._commands = []

    def register(
        self,
        command,
    ):

        self._commands.append(
            command,
        )

    def commands(
        self,
    ):

        return self._commands
