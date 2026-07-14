from jarvis.resources.repository import ResourceRepository

from jarvis.search.index import SearchIndex

from jarvis.search.loaders.file_loader import FileLoader


index = SearchIndex()

repository = ResourceRepository()

loader = FileLoader()

loader.load(
    index,
    repository,
)

print("----------------------------------")
print("Items en el índice:", len(index.all()))
print("Recursos:", len(repository.all()))
print("----------------------------------")

for item in index.all()[:20]:

    print(item)
