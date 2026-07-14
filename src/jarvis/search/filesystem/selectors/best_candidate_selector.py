from jarvis.search.filesystem.ranking.candidate import (
    FileCandidate,
)


class BestCandidateSelector:

    def select(
        self,
        candidates: list[FileCandidate],
    ) -> FileCandidate | None:

        if not candidates:
            return None

        return candidates[0]
