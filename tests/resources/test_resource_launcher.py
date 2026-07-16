from jarvis.resources.launcher import ResourceLauncher

from jarvis.search.search import SearchEngine


engine = SearchEngine()

resource = engine.resolve(
    "firefox",
)

launcher = ResourceLauncher()

launcher.open(
    resource,
)

engine.stop()
