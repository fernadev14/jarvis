from jarvis.search.item import SearchItem


class SearchIndex:

    def __init__(self):

        self._items: dict[str, SearchItem] = {}

    def add(
        self,
        item: SearchItem,
    ):

        self._items[item.resource_id] = item

    def get(
        self,
        resource_id: str,
    ):

        return self._items.get(resource_id)

    def remove(
        self,
        resource_id: str,
    ):

        self._items.pop(
            resource_id,
            None,
        )

    def replace(
        self,
        item: SearchItem,
    ):

        self._items[item.resource_id] = item

    def contains(
        self,
        resource_id: str,
    ):

        return resource_id in self._items

    def all(self):

        return list(
            self._items.values()
        )
