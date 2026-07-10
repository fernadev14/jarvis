from jarvis.search.matcher import Matcher
from jarvis.search.result import SearchResult


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

            if score < 50:
                continue

            results.append(
                SearchResult(
                    item=item,
                    score=score,
                )
            )

        results.sort(
            key=lambda r: r.score,
            reverse=True,
        )

        return results
