from jarvis.files.indexer import FileIndexer


class FileLoader:

    def load(
        self,
        index,
        repository,
    ):

        indexer = FileIndexer()

        for resource in indexer.scan():

            repository.add(resource)

            index.add(
                resource.to_search_item()
            )
