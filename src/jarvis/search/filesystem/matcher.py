from rapidfuzz import fuzz


class FileMatcher:

    def __init__(
        self,
        min_score=70,
    ):
        self.min_score = min_score

    def search(
        self,
        query,
        index,
    ):

        results = []

        query = self.normalize(query)

        query_tokens = self.tokenize(query)

        for record in index:

            score = self.score(
                query,
                query_tokens,
                record.name,
            )

            if score < self.min_score:
                continue

            results.append(
                (
                    score,
                    record,
                )
            )

        return results

    def score(
        self,
        query,
        query_tokens,
        filename,
    ):

        filename = self.normalize(filename)

        filename_tokens = self.tokenize(filename)

        scores = [

            self.exact(
                query,
                filename,
            ),

            self.prefix(
                query,
                filename,
            ),

            self.partial(
                query,
                filename,
            ),

            self.token_score(
                query_tokens,
                filename_tokens,
            ),

        ]

        return max(scores)

    def exact(
        self,
        query,
        filename,
    ):

        if query == filename:

            return 100

        return 0

    def prefix(
        self,
        query,
        filename,
    ):

        if filename.startswith(query):

            return 95

        return 0

    def partial(
        self,
        query,
        filename,
    ):

        return max(

            fuzz.partial_ratio(
                query,
                filename,
            ),

            fuzz.token_sort_ratio(
                query,
                filename,
            ),

            fuzz.ratio(
                query,
                filename,
            ),
        )

    def token_score(
        self,
        query_tokens,
        filename_tokens,
    ):

        if not query_tokens:

            return 0

        total = 0

        for token in query_tokens:

            best = 0

            for candidate in filename_tokens:

                best = max(
                    best,
                    fuzz.ratio(
                        token,
                        candidate,
                    ),
                )

            total += best

        return total / len(query_tokens)

    def normalize(
        self,
        text,
    ):

        return text.lower().strip()

    def tokenize(
        self,
        text,
    ):

        return [
            token
            for token in text.split()
            if token
        ]
