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
    "firefox lo puedes abrir",
    "el contrato puedes abrirlo",
    "por favor firefox",
    "github por favor",
    "documentos por favor",
    "el archivo llamado contrato",
    "abre la aplicacion firefox",
    "abre la carpeta descargas",
    "abre el archivo contrato",
    "abre github en brave",
    "abre youtube con firefox",
]

for t in tests:

    print()

    print(t)

    print(nlu.understand(t))
