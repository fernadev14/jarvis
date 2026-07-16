from jarvis.search.filesystem.filesystem_runtime import (
    FilesystemRuntime,
)

from jarvis.search.search_index_builder import (
    SearchIndexBuilder,
)


class SearchRuntime:

    def __init__(self):

        self.context = SearchIndexBuilder().build()

        self.filesystem = FilesystemRuntime(
            self.context.service,
        )

    def start(self):

        self.filesystem.start()

        return self.context

    def stop(self):

        self.filesystem.stop()
