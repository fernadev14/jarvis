from jarvis.skills.registry import SkillRegistry
from jarvis.skills.open import OpenSkill


class SkillManager:

    def __init__(self):

        registry = SkillRegistry()

        registry.register(OpenSkill())

        self.registry = registry

    def find(self, understanding):

        for skill in self.registry.all():

            if skill.intent == understanding.intent:
                return skill

        return None
