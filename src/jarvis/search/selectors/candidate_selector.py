from jarvis.search.result import SearchResult


class CandidateSelector:

    MIN_SCORE = 60

    DELTA = 5

    def select(
        self,
        results: list[SearchResult],
    ):

        if not results:
            return []

        best = results[0]

        candidates = []

        for result in results:

            if result.score < self.MIN_SCORE:
                continue

            if best.score - result.score <= self.DELTA:

                candidates.append(result)

        return candidates
