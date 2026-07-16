from watchdog.observers import Observer

from jarvis.search.filesystem.watchers.watchdog_handler import (
    WatchdogHandler,
)


class FileWatcher:

    def __init__(
        self,
        directory,
        updater,
    ):

        self.directory = directory

        self.observer = Observer()

        self.handler = WatchdogHandler(
            updater,
        )

    def start(self):

        self.observer.schedule(
            self.handler,
            self.directory,
            recursive=True,
        )

        self.observer.start()

    def stop(self):

        self.observer.stop()

        self.observer.join()
