from jarvis.search.filesystem.watchers.file_watcher import (
    FileWatcher,
)

watcher = FileWatcher()

print(watcher.running)

watcher.start()

print(watcher.running)

watcher.stop()

print(watcher.running)
