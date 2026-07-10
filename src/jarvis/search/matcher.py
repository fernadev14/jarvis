from jarvis.search.scorers.alias import AliasScorer
from jarvis.search.scorers.exact import ExactScorer
from jarvis.search.scorers.fuzzy import FuzzyScorer


class Matcher:

    def __init__(self):

        self.exact = ExactScorer()

        self.alias = AliasScorer()

        self.fuzzy = FuzzyScorer()

    def score(
        self,
        query,
        item,
    ):

        scores = [

            self.exact.score(
                query,
                item.name,
            ),

            self.alias.score(
                query,
                item.aliases,
            ),

            self.fuzzy.score(
                query,
                item.name,
            ),
        ]

        for alias in item.aliases:

            scores.append(

                self.fuzzy.score(
                    query,
                    alias,
                )
            )

        return max(scores)
