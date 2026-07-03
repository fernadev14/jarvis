from pydantic import BaseModel

from jarvis.models.entity_type import EntityType


class ResolvedEntity(BaseModel):

    name: str

    entity_type: EntityType

    executable: str | None = None

    url: str | None = None

    path: str | None = None
