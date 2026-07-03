from enum import Enum


class ResourceType(str, Enum):

    APPLICATION = "application"

    WEBSITE = "website"

    FOLDER = "folder"

    FILE = "file"

    PROJECT = "project"

    UNKNOWN = "unknown"
