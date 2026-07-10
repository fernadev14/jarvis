from rapidfuzz import fuzz


class FuzzyScorer:

    def score(
        self,
        query: str,
        text: str,
    ) -> float:

        if not query or not text:
            return 0

        return max(
            fuzz.ratio(query, text),
            fuzz.partial_ratio(query, text),
            fuzz.token_sort_ratio(query, text),
        )
