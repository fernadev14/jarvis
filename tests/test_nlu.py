from jarvis.nlu.language_understanding import LanguageUnderstanding

nlu = LanguageUnderstanding()

tests = [
    "abre firefox",
    "abre youtube",
    "abre github",
    "abre visual",
    "hola",
]

for t in tests:

    print()

    print(t)

    print(nlu.understand(t))
