from jarvis.search.scorers.alias import AliasScorer
from jarvis.search.scorers.exact import ExactScorer
from jarvis.search.scorers.fuzzy import FuzzyScorer

from jarvis.search.preprocessing.normalizer import (
    SearchNormalizer,
)
from jarvis.search.preprocessing.tokenizer import (
    SearchTokenizer,
)


class Matcher:

    def __init__(self):

        self.exact = ExactScorer()
        self.alias = AliasScorer()
        self.fuzzy = FuzzyScorer()

        self.normalizer = SearchNormalizer()
        self.tokenizer = SearchTokenizer()

    def score(
        self,
        query,
        item,
    ):

        query = self.normalizer.normalize(
            query,
        )

        query_tokens = self.tokenizer.tokenize(
            query,
        )

        candidates = [

            item.name,

            *item.aliases,
        ]

        best = 0

        for candidate in candidates:

            candidate = self.normalizer.normalize(
                candidate,
            )

            candidate_tokens = self.tokenizer.tokenize(
                candidate,
            )

            for query_word in query_tokens:

                for candidate_word in candidate_tokens:

                    score = self.fuzzy.score(

                        query_word,

                        candidate_word,
                    )

                    best = max(
                        best,
                        score,
                    )

        return best
