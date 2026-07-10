from pydantic import BaseModel

from jarvis.models.resource_type import ResourceType


class Resource(BaseModel):

    id: str

    name: str

    resource_type: ResourceType

    executable: str | None = None

    url: str | None = None

    path: str | None = None
