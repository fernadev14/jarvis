from jarvis.search.loaders.file_loader import FileLoader
from jarvis.search.index import SearchIndex
from jarvis.resources.repository import ResourceRepository
from jarvis.search.index_service import IndexService

index = SearchIndex()
repository = ResourceRepository()

service = IndexService(
    index=index,
    repository=repository,
)

loader = FileLoader()

loader.load(
    service,
)

print(len(index.all()))
