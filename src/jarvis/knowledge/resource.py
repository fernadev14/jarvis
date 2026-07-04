from pydantic import BaseModel


class KnowledgeResource(BaseModel):

    name: str

    type: str

    aliases: list[str]

    executable: str | None = None

    url: str | None = None

    path: str | None = None
