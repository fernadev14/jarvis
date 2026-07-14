from jarvis.search.item import SearchItem


class ApplicationIndexer:

    IGNORE = {
        "",
        "python",
        "python3",
        "vim",
        "vi",
        "nano",
        "bash",
        "sh",
    }

    def index(
        self,
        app,
        resource,
    ):

        name = resource.name.strip()

        if not name:
            return None

        if name.lower() in self.IGNORE:
            return None

        aliases = list(app.aliases)

        aliases.append(name.lower())

        aliases = list(dict.fromkeys(aliases))

        return SearchItem(
            resource_id=resource.id,
            name=name,
            aliases=aliases,
        )
