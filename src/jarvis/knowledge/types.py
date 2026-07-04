from enum import Enum


class KnowledgeType(str, Enum):

    APPLICATION = "application"

    WEBSITE = "website"

    FOLDER = "folder"

    FILE = "file"

    PROJECT = "project"
