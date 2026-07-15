from jarvis.resources.repository import ResourceRepository

from jarvis.search.index import SearchIndex

from jarvis.search.lifecycle.lifecycle_manager import (
    LifecycleManager,
)


class FakeKnowledgeProvider:

    def load(
        self,
        index,
        repository,
    ):

        print("Cargando Knowledge")


class FakeDesktopProvider:

    def load(
        self,
        index,
        repository,
    ):

        print("Cargando Desktop")


class FakeFilesystemProvider:

    def load(
        self,
        index,
        repository,
    ):

        print("Cargando Filesystem")


manager = LifecycleManager()

manager.register(
    FakeKnowledgeProvider(),
)

manager.register(
    FakeDesktopProvider(),
)

# Intentamos registrar otro DesktopProvider
manager.register(
    FakeDesktopProvider(),
)

manager.register(
    FakeFilesystemProvider(),
)

manager.load(
    SearchIndex(),
    ResourceRepository(),
)
