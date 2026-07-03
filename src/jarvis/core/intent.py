from enum import Enum


class Intent(Enum):
    CHAT = "chat"

    OPEN_APP = "open_app"

    SHUTDOWN = "shutdown"

    RESTART = "restart"

    LIST_FILES = "list_files"

    UNKNOWN = "unknown"
