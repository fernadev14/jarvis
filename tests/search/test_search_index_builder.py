from jarvis.search.search_index_builder import SearchIndexBuilder


builder = SearchIndexBuilder()

context = builder.build()

index = context.index
repository = context.repository

print("----------------------------------")
print("Items índice :", len(index.all()))
print("Recursos     :", len(repository.all()))
print("----------------------------------")
print()

for item in index.all()[:20]:
    print(item)

print()
print("Recursos sin SearchItem")
print("-----------------------")

indexed = {item.resource_id for item in index.all()}

for resource in repository.all():

    if resource.id not in indexed:

        print(resource)
