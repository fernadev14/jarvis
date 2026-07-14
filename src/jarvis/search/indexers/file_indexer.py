from jarvis.search.item import SearchItem


class FileIndexer:

    def index(
        self,
        resource,
    ):

        return SearchItem(

            resource_id=resource.id,

            name=resource.name,

            aliases=[],
        )
