from time import sleep

from jarvis.resources.repository import ResourceRepository

from jarvis.search.index import SearchIndex
from jarvis.search.index_service import IndexService

from jarvis.search.filesystem.updaters.filesystem_updater import (
    FilesystemUpdater,
)

from jarvis.search.filesystem.watchers.file_watcher import (
    FileWatcher,
)

from jarvis.platforms.userdirs.user_directories import (
    UserDirectories,
)

directories = UserDirectories()

index = SearchIndex()

repository = ResourceRepository()

service = IndexService(
    index=index,
    repository=repository,
)

updater = FilesystemUpdater(
    service,
)

watcher = FileWatcher(
    directory=directories.documents(),
    updater=updater,
)

watcher.start()

print("Watcher iniciado")
print("Crea, modifica o elimina un archivo en Documents")
print("Ctrl+C para salir")

try:

    while True:
        sleep(1)

except KeyboardInterrupt:

    watcher.stop()
