from jarvis.search.item import SearchItem


class WebExtractor:

    def extract(
        self,
        repository,
    ):

        items = []

        for resource in repository.all():

            if resource.resource_type.value != "website":
                continue

            items.append(
                SearchItem(
                    resource_id=resource.id,
                    name=resource.name,
                    aliases=resource.aliases,
                )
            )

        return items
