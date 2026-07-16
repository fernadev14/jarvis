from pathlib import Path

from watchdog.events import (
    FileSystemEventHandler,
)

from jarvis.search.filesystem.events.filesystem_event import (
    FilesystemEvent,
)

from jarvis.search.filesystem.events.filesystem_event_type import (
    FilesystemEventType,
)


class WatchdogHandler(FileSystemEventHandler):

    def __init__(
        self,
        updater,
    ):

        self.updater = updater

    def _dispatch(
        self,
        event_type,
        path,
    ):

        if event_type == FilesystemEventType.CREATED:

            self.updater.created(
                Path(path),
            )

        elif event_type == FilesystemEventType.MODIFIED:

            self.updater.modified(
                Path(path),
            )

        elif event_type == FilesystemEventType.DELETED:

            self.updater.deleted(
                Path(path),
            )

    def on_created(
        self,
        event,
    ):

        print("WATCHDOG CREATED:", event.src_path)

        if event.is_directory:
            return

        self._dispatch(
            FilesystemEventType.CREATED,
            event.src_path,
        )

    def on_modified(
        self,
        event,
    ):

        print("WATCHDOG MODIFIED:", event.src_path)
        if event.is_directory:
            return

        self._dispatch(
            FilesystemEventType.MODIFIED,
            event.src_path,
        )

    def on_deleted(
        self,
        event,
    ):

        print("WATCHDOG DELETED:", event.src_path)
        if event.is_directory:
            return

        self._dispatch(
            FilesystemEventType.DELETED,
            event.src_path,
        )

    def on_moved(
        self,
        event,
    ):

        print("WATCHDOG MOVED:", event.src_path, "->", event.dest_path)
        if event.is_directory:
            return

        self._dispatch(
            FilesystemEventType.MOVED,
            event.dest_path,
        )
