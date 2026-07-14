from jarvis.search.item import SearchItem


class KnowledgeIndexer:

    def index(
        self,
        resource,
        aliases,
    ):

        return SearchItem(
            resource_id=resource.id,
            name=resource.name,
            aliases=aliases,
        )
