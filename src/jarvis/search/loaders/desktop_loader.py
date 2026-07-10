from jarvis.models.resource import Resource
from jarvis.models.resource_type import ResourceType

from jarvis.platforms.discovery.factory import DiscoveryFactory

from jarvis.resources.repository import ResourceRepository

from jarvis.search.index import SearchIndex
from jarvis.search.item import SearchItem


class DesktopLoader:

    def __init__(self):

        self.repository = DiscoveryFactory.create()

    def load(
        self,
        index: SearchIndex,
        repository: ResourceRepository,
    ):

        for app in self.repository.applications:

            resource = Resource(

                id=f"desktop:{app.desktop_file}",

                name=app.name,

                resource_type=ResourceType.APPLICATION,

                executable=app.executable,
            )

            repository.add(resource)

            index.add(

                SearchItem(

                    resource_id=resource.id,

                    name=app.name,

                    aliases=app.aliases,
                )
            )
