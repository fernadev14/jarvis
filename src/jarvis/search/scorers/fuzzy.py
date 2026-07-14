from rapidfuzz import fuzz

from jarvis.search.scorers.scorer import Scorer


class FuzzyScorer(Scorer):

    def score(
        self,
        query,
        candidate,
    ):

        if not query or not candidate:
            return 0

        return max(
            fuzz.ratio(query, candidate),
            fuzz.partial_ratio(query, candidate),
            fuzz.token_sort_ratio(query, candidate),
        )
