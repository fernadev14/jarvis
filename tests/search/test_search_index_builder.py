from jarvis.search.search_index_builder import SearchIndexBuilder


builder = SearchIndexBuilder()

index, repository = builder.build()

print("----------------------------------")
print("Items índice :", len(index.all()))
print("Recursos     :", len(repository.all()))
print("----------------------------------")

print()

for item in index.all()[:20]:

    print(item)


item_ids = {
    item.resource_id
    for item in index.all()
}

resource_ids = {
    resource.id
    for resource in repository.all()
}

missing = resource_ids - item_ids

print()
print("Recursos sin SearchItem")
print("-----------------------")

for resource_id in missing:
    print(resource_id)
