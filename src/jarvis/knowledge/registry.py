from pathlib import Path
from jarvis.knowledge.types import KnowledgeType

import yaml

from jarvis.knowledge.resource import KnowledgeResource


class KnowledgeRegistry:

    def __init__(self):

        self.resources: dict[str, KnowledgeResource] = {}

        self.load()

    def load(self):

        file = (
            Path(__file__).parent
            / "resources.yml"
        )

        if not file.exists():

            return

        with open(file, "r", encoding="utf8") as f:

            data = yaml.safe_load(f) or {}

        for name, info in data.items():

            self.resources[name] = KnowledgeResource(
                name=name,
                type=KnowledgeType(info["type"]),
                aliases=info.get("aliases", []),
                executable=info.get("executable"),
                url=info.get("url"),
                path=info.get("path"),
            )

    def find(self, text: str):

        text = text.lower().strip()

        for resource in self.resources.values():

            if text == resource.name:

                return resource

            if text in resource.aliases:

                return resource

        return None
