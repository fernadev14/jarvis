from time import sleep

from jarvis.resources.repository import (
    ResourceRepository,
)

from jarvis.search.index import (
    SearchIndex,
)

from jarvis.search.index_service import (
    IndexService,
)

from jarvis.search.filesystem.filesystem_runtime import (
    FilesystemRuntime,
)

index = SearchIndex()

repository = ResourceRepository()

service = IndexService(
    index=index,
    repository=repository,
)

runtime = FilesystemRuntime(
    service=service,
)

runtime.start()

print("Watcher iniciado")
print("Crea, modifica o elimina un archivo en Documents")
print("Ctrl+C para salir")

try:

    while True:
        sleep(1)

except KeyboardInterrupt:

    runtime.stop()
