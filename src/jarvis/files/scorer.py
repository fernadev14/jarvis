from difflib import SequenceMatcher


class Scorer:

    def score(
        self,
        query: str,
        candidate: str,
    ) -> float:

        query = query.lower().strip()

        candidate = candidate.lower().strip()

        return SequenceMatcher(
            None,
            query,
            candidate,
        ).ratio()
