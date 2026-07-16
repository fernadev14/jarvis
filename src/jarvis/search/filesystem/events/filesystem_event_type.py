from enum import Enum


class FilesystemEventType(str, Enum):

    CREATED = "created"

    MODIFIED = "modified"

    DELETED = "deleted"

    MOVED = "moved"
