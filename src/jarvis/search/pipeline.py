from jarvis.search.selectors.candidate_selector import (
    CandidateSelector,
)


class SearchPipeline:

    def __init__(
        self,
        rewriter,
        ranking,
        selector,
        repository,
    ):

        self.rewriter = rewriter

        self.ranking = ranking

        self.selector = selector

        self.repository = repository

    def search(

        self,
        query,
        items,
        context="",
    ):
        query = self.rewriter.rewrite(
            query,
        )

        ranked = self.ranking.rank(
            query,
            items,
            context,
        )

        return self.selector.select(
            ranked,

        )

    def resolve(
        self,
        query,
        items,
        context="",
    ):
        candidates = self.search(
            query,
            items,
            context,
        )
        if not candidates:
            return None
        return self.repository.get(
            candidates[0].item.resource_id
        )
