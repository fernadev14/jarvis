from pathlib import Path
from jarvis.knowledge.types import KnowledgeType
from rapidfuzz import fuzz
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

    def find_best(self, text: str):

        text = text.lower().strip()

        best_resource = None
        best_score = 0

        for resource in self.resources.values():

            candidates = [
                resource.name,
                *resource.aliases,
            ]

            for candidate in candidates:

                score = fuzz.WRatio(
                    text,
                    candidate.lower(),
                )

                if score > best_score:

                    best_score = score
                    best_resource = resource

        if best_score >= 70:

            return best_resource

        return None
