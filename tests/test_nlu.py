from jarvis.nlu.language_understanding import LanguageUnderstanding

nlu = LanguageUnderstanding()

tests = [
    "abre firefox",
    "abre youtube",
    "abre descargas",
    "abre contrato",
    "hola",
    "abreme firefox",
    "abrir firefox",
    "abrirme outlook",
    "buenas",
    "hey",
    "puedes abrir firefox",
    "podrias abrir mysql",
    "quiero abrir youtube",
    "necesito abrir google",
    "me ayudas a abrir github",
]

for t in tests:

    print()

    print(t)

    print(nlu.understand(t))
