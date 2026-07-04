from jarvis.core.action_router import ActionRouter
from jarvis.nlu.language_understanding import LanguageUnderstanding

router = ActionRouter()
nlu = LanguageUnderstanding()

tests = [
    "abre firefox",
    "abre youtube",
    "hola",
]

for text in tests:

    print("-" * 40)
    print(text)

    understanding = nlu.understand(text)

    print(understanding)

    action = router.route(understanding)

    print(action)
