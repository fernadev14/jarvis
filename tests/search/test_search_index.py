from jarvis.search.index import SearchIndex
from jarvis.search.item import SearchItem


index = SearchIndex()

item = SearchItem(
    resource_id="file:contrato.pdf",
    name="contrato",
    aliases=[],
)

print(index.contains("file:contrato.pdf"))

index.add(item)

print(index.contains("file:contrato.pdf"))

print(index.get("file:contrato.pdf"))

index.remove("file:contrato.pdf")

print(index.contains("file:contrato.pdf"))
