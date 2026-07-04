from pydantic import BaseModel

from jarvis.models.resource import Resource
from jarvis.models.resource_type import ResourceType


class Understanding(BaseModel):

    intent: str

    entity: str

    resource_type: ResourceType

    resource: Resource | None = None
