from jarvis.nlu.language_understanding import LanguageUnderstanding

nlu = LanguageUnderstanding()

tests = [
    "abre firefox",
    "abre youtube",
    "abre descargas",
    "abre contrato.pdf",
    "hola",
]

for t in tests:

    print()

    print(t)

    print(nlu.understand(t))
