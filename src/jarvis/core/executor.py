from jarvis.core.brain import Brain

from jarvis.skills.manager import SkillManager

from jarvis.search.search import SearchEngine

from jarvis.search.filesystem.search_engine import (
    FilesystemSearchEngine,
)


class Executor:

    def __init__(self):

        self.skills = SkillManager()

        self.search = SearchEngine()

        self.files = FilesystemSearchEngine()

        self.brain = Brain()

    def execute(
        self,
        understanding,
        message,
    ):

        skill = self.skills.find(
            understanding,
        )

        if skill:

            result = skill.execute(
                understanding,
            )

            return result.message

        return self.brain.ask(
            message,
        )
