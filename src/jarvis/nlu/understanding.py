from pydantic import BaseModel

from jarvis.models.resource import Resource
from jarvis.models.resource_type import ResourceType


class Understanding(BaseModel):

    intent: str

    entity: str

    context: str = ""

    tool: str = ""

    location: str = ""

    resource_type: ResourceType = ResourceType.UNKNOWN

    resource: Resource | None = None
