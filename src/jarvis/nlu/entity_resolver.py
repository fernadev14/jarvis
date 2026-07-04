from jarvis.knowledge.applications import ApplicationRegistry
from jarvis.knowledge.websites import WebsiteRegistry
from jarvis.models.resource import Resource
from jarvis.models.resource_type import ResourceType


class EntityResolver:

    def __init__(self):

        self.apps = ApplicationRegistry()

        self.websites = WebsiteRegistry()

    def resolve(self, entity: str) -> Resource | None:

        app = self.apps.find(entity)

        if app is not None:

            return Resource(
                name=app.name,
                resource_type=ResourceType.APPLICATION,
                executable=app.executable,
            )

        site = self.websites.find(entity)

        if site is not None:

            return Resource(
                name=site["name"],
                resource_type=ResourceType.WEBSITE,
                url=site["url"],
            )

        return None
