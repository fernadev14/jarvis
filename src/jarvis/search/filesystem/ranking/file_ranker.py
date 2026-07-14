from jarvis.search.filesystem.ranking.candidate import (
    FileCandidate,
)


class FileRanker:

    def rank(
        self,
        matches,
    ):

        candidates = []

        for score, record in matches:

            candidates.append(
                FileCandidate(
                    record=record,
                    score=score,
                )
            )

        candidates.sort(

            key=lambda x: x.score,

            reverse=True,

        )

        return candidates
