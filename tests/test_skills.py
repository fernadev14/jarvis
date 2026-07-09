from jarvis.skills.manager import SkillManager
from jarvis.skills.registry import SkillRegistry
from jarvis.skills.open import OpenSkill


registry = SkillRegistry()

registry.register(OpenSkill())

manager = SkillManager(registry)

print(manager.find(type("Dummy", (), {"intent": "open"})))
print(manager.find(type("Dummy", (), {"intent": "chat"})))
