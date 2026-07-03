from jarvis.knowledge.applications import ApplicationRegistry
from jarvis.knowledge.websites import WebsiteRegistry

from jarvis.nlu.understanding import EntityType


class EntityResolver:

    def __init__(self):

        self.apps = ApplicationRegistry()

        self.webs = WebsiteRegistry()

    def resolve(self, entity: str):

        if self.apps.find(entity):

            return EntityType.APPLICATION

        if self.webs.find(entity):

            return EntityType.WEBSITE

        return EntityType.UNKNOWN
