from jarvis.search.item import SearchItem


class KnowledgeIndexer:

    def index(
        self,
        item,
        resource,
    ):

        return SearchItem(
            resource_id=resource.id,
            name=resource.name,
            aliases=item.aliases,
        )
