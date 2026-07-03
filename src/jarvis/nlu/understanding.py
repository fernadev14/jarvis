from enum import Enum

from pydantic import BaseModel


class EntityType(str, Enum):

    APPLICATION = "application"

    WEBSITE = "website"

    LOCATION = "location"

    FILE = "file"

    UNKNOWN = "unknown"


class Understanding(BaseModel):

    intent: str

    entity: str

    entity_type: EntityType
