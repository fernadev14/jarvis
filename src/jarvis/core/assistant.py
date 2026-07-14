from jarvis.core.executor import Executor

from jarvis.nlu.language_understanding import (
    LanguageUnderstanding,
)


class Assistant:

    def __init__(self):

        self.nlu = LanguageUnderstanding()

        self.executor = Executor()

    def chat(
        self,
        message,
    ):

        understanding = self.nlu.understand(
            message,
        )

        return self.executor.execute(
            understanding,
            message,
        )
