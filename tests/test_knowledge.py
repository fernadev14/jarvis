from jarvis.knowledge.registry import KnowledgeRegistry

registry = KnowledgeRegistry()

tests = [
    "firefox",
    "google",
    "github",
    "youtube",
    "descargas",
    "documentos",
    "escritorio",
    "imagenes",
    "musica",
]

for test in tests:

    print("-" * 40)

    print(test)

    print(registry.find(test))
