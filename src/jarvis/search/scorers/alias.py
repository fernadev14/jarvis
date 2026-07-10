class AliasScorer:

    def score(
        self,
        query: str,
        aliases: list[str],
    ) -> float:

        if query in aliases:
            return 100

        return 0
