from pydantic import BaseModel

from jarvis.knowledge.types import KnowledgeType


class KnowledgeResource(BaseModel):

    name: str

    type: KnowledgeType

    aliases: list[str]

    executable: str | None = None

    url: str | None = None

    path: str | None = None
