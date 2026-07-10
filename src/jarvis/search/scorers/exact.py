class ExactScorer:

    def score(
        self,
        query: str,
        text: str,
    ) -> float:

        if not query or not text:
            return 0

        if query == text:
            return 100

        return 0
