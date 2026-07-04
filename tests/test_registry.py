from jarvis.knowledge.applications import ApplicationRegistry

registry = ApplicationRegistry()

tests = [
    "firefox",
    "google",
    "chrome",
    "visual",
    "terminal",
    "hola"
]

for test in tests:

    app = registry.find(test)

    print(test, "->", app)
