from pydantic import BaseModel

from jarvis.models.entity_type import EntityType
from jarvis.models.resolved_entity import ResolvedEntity


class Understanding(BaseModel):

    intent: str

    entity: str

    entity_type: EntityType

    resolved: ResolvedEntity | None = None
