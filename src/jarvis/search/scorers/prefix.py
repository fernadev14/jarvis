from jarvis.search.scorers.scorer import Scorer


class PrefixScorer(Scorer):

    def score(
        self,
        query,
        candidate,
    ):

        if candidate.startswith(query):
            return 95

        return 0
