from jarvis.nlu.language_understanding import LanguageUnderstanding


nlu = LanguageUnderstanding()


def check(text):

    u = nlu.understand(text)

    return (
        u.intent,
        u.entity,
        u.tool,
        u.location,
    )


assert check("abre firefox") == (
    "open",
    "firefox",
    "",
    "",
)

assert check("abre github en firefox") == (
    "open",
    "github",
    "firefox",
    "",
)

assert check("abre contrato desde documentos") == (
    "open",
    "contrato",
    "",
    "documentos",
)

assert check("por favor abre visual studio code") == (
    "open",
    "visual studio code",
    "",
    "",
)
