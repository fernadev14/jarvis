from pathlib import Path

from watchdog.events import (
    FileSystemEventHandler,
)


class WatchdogHandler(FileSystemEventHandler):

    def __init__(
        self,
        updater,
    ):

        self.updater = updater

    def on_created(
        self,
        event,
    ):

        if event.is_directory:
            return

        print(
            "WATCHDOG CREATED:",
            event.src_path,
        )

        self.updater.created(
            Path(event.src_path),
        )

    def on_modified(
        self,
        event,
    ):

        if event.is_directory:
            return

        print(
            "WATCHDOG MODIFIED:",
            event.src_path,
        )

        self.updater.modified(
            Path(event.src_path),
        )

    def on_deleted(
        self,
        event,
    ):

        if event.is_directory:
            return

        print(
            "WATCHDOG DELETED:",
            event.src_path,
        )

        self.updater.deleted(
            Path(event.src_path),
        )

    def on_moved(
        self,
        event,
    ):

        if event.is_directory:
            return

        print(
            "WATCHDOG MOVED:",
            event.src_path,
            "->",
            event.dest_path,
        )

        self.updater.deleted(
            Path(event.src_path),
        )

        self.updater.created(
            Path(event.dest_path),
        )
