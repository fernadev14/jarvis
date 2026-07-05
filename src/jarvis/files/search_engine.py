from pathlib import Path

from jarvis.files.candidate_filter import CandidateFilter
from jarvis.files.finder import FileFinder
from jarvis.files.scorer import Scorer


class SearchEngine:

    MIN_SCORE = 0.80

    def __init__(self):

        self.finder = FileFinder()

        self.filter = CandidateFilter()

        self.scorer = Scorer()

    def search(
        self,
        query: str,
    ) -> Path | None:

        files = self.finder.find()

        candidates = self.filter.filter(
            query,
            files,
        )

        if not candidates:

            return None

        best_file = None

        best_score = 0.0

        for file in candidates:

            stem_score = self.scorer.score(
                query,
                file.stem,
            )

            full_score = self.scorer.score(
                query,
                file.name,
            )

            score = max(
                stem_score,
                full_score,
            )

            if score > best_score:

                best_score = score

                best_file = file

        if best_score < self.MIN_SCORE:

            return None

        return best_file
