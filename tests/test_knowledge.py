from jarvis.knowledge.registry import KnowledgeRegistry

registry = KnowledgeRegistry()

tests = [
    "firefox",
    "google",
    "visual",
    "github",
    "youtube",
    "hola",
]

for test in tests:

    print("-" * 40)

    print(test)

    print(registry.find(test))
