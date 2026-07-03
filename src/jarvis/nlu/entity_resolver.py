from jarvis.knowledge.applications import ApplicationRegistry
from jarvis.knowledge.websites import WebsiteRegistry
from jarvis.models.resolved_entity import ResolvedEntity
from jarvis.models.entity_type import EntityType


class EntityResolver:

    def __init__(self):

        self.apps = ApplicationRegistry()

        self.websites = WebsiteRegistry()

    def resolve(self, entity: str) -> ResolvedEntity | None:

        app = self.apps.find(entity)

        if app is not None:

            return ResolvedEntity(
                name=app.name,
                entity_type=EntityType.APPLICATION,
                executable=app.executable,
            )

        site = self.websites.find(entity)

        if site is not None:

            return ResolvedEntity(
                name=site["name"],
                entity_type=EntityType.WEBSITE,
                url=site["url"],
            )

        return None
