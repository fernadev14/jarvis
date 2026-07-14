from jarvis.search.rewriter.rules import (
    RewriteRules,
)


class QueryRewriter:

    def __init__(self):

        self.rules = RewriteRules()

    def rewrite(
        self,
        query: str,
    ):

        return self.rules.apply(query)
