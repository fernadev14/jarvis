from enum import Enum


class EntityType(str, Enum):

    APPLICATION = "application"

    WEBSITE = "website"

    LOCATION = "location"

    FILE = "file"

    UNKNOWN = "unknown"
