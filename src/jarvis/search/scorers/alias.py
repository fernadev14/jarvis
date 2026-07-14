from jarvis.search.scorers.scorer import Scorer


class AliasScorer(Scorer):

    def score(
        self,
        query,
        aliases,
    ):

        if query in aliases:
            return 100

        return 0
