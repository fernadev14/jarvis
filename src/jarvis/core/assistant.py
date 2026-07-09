from jarvis.core.brain import Brain
from jarvis.nlu.language_understanding import LanguageUnderstanding
from jarvis.skills.manager import SkillManager


class Assistant:

    def __init__(self):

        self.brain = Brain()

        self.nlu = LanguageUnderstanding()

        self.skills = SkillManager()

    def chat(self, message: str):

        understanding = self.nlu.understand(message)

        skill = self.skills.find(understanding)

        if skill:

            result = skill.execute(understanding)

            return result.message

        return self.brain.ask(message)
