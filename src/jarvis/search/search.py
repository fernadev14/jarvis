from jarvis.search.ranking import Ranking

from jarvis.search.rewriter.query_rewriter import (
    QueryRewriter,
)

from jarvis.search.selectors.candidate_selector import (
    CandidateSelector,
)

from jarvis.search.pipeline import SearchPipeline

from jarvis.search.search_runtime import (
    SearchRuntime,
)


class SearchEngine:

    def __init__(self):

        self.runtime = SearchRuntime()
        self.context = self.runtime.start()
        self.index = self.context.index
        self.repository = self.context.repository

        #
        # componentes del buscador
        #

        self.pipeline = SearchPipeline(
            rewriter=QueryRewriter(),
            ranking=Ranking(),
            selector=CandidateSelector(),
            repository=self.repository,
        )

    def search(
        self,
        query: str,
        context: str = "",
    ):

        return self.pipeline.search(
            query=query,
            items=self.index.all(),
            context=context,
        )

    def resolve(
        self,
        query: str,
        context: str = "",
    ):

        return self.pipeline.resolve(
            query=query,
            items=self.index.all(),
            context=context,
        )

    def get_resource(
        self,
        resource_id: str,
    ):

        return self.repository.get(resource_id)

    def search_file(
        self,
        query,
    ):

        return self.files.search(query)

    def stop(self):

        self.runtime.stop()
