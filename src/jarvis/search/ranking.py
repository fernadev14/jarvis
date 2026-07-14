from jarvis.search.matcher import Matcher
from jarvis.search.result import SearchResult
from jarvis.search.confidence import Confidence


class Ranking:

    def __init__(self):

        self.matcher = Matcher()

    def rank(
        self,
        query: str,
        items,
        context: str = "",
    ):

        results = []

        for item in items:

            score = self.matcher.score(
                query,
                item,
            )

            confidence = self.confidence(score)

            if confidence == Confidence.NONE:
                continue

            results.append(
                SearchResult(
                    item=item,
                    score=score,
                    confidence=confidence,
                )
            )

        results.sort(
            key=lambda r: r.score,
            reverse=True,
        )

        return results

    def confidence(self, score: float) -> Confidence:

        if score >= 95:
            return Confidence.HIGH

        if score >= 80:
            return Confidence.MEDIUM

        if score >= 60:
            return Confidence.LOW

        return Confidence.NONE
