from jarvis.models.resource import Resource
from jarvis.models.resource_type import ResourceType

from jarvis.platforms.discovery.factory import DiscoveryFactory

from jarvis.search.indexers.application_indexer import (
    ApplicationIndexer,
)


class DesktopLoader:

    def __init__(self):

        self.repository = DiscoveryFactory.create()

        self.indexer = ApplicationIndexer()

    def load(
        self,
        service,
    ):

        for app in self.repository.applications:

            resource = Resource(

                id=f"desktop:{app.desktop_file}",

                name=app.name,

                resource_type=ResourceType.APPLICATION,

                executable=app.executable,
            )

            item = self.indexer.index(
                app,
                resource,
            )

            if item is None:
                continue

            service.add(
                resource,
                item,
            )
