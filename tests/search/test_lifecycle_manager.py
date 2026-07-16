from jarvis.resources.repository import ResourceRepository

from jarvis.search.index import SearchIndex
from jarvis.search.index_service import IndexService

from jarvis.search.lifecycle.lifecycle_manager import (
    LifecycleManager,
)


class FakeKnowledgeProvider:

    def load(
        self,
        service,
    ):

        print("Cargando Knowledge")


class FakeDesktopProvider:

    def load(
        self,
        service,
    ):

        print("Cargando Desktop")


class FakeFilesystemProvider:

    def load(
        self,
        service,
    ):

        print("Cargando Filesystem")


index = SearchIndex()
repository = ResourceRepository()

service = IndexService(
    index=index,
    repository=repository,
)

providers = [

    FakeKnowledgeProvider(),

    FakeDesktopProvider(),

    FakeFilesystemProvider(),

]

manager = LifecycleManager()

manager.load(
    providers,
    service,
)
