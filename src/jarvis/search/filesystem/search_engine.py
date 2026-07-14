from jarvis.platforms.userdirs.user_directories import (
    UserDirectories,
)

from jarvis.search.filesystem.matcher import (
    FileMatcher,
)

from jarvis.search.filesystem.ranking.file_ranker import (
    FileRanker,
)

from jarvis.search.filesystem.scanner import (
    FileScanner,
)

from jarvis.search.filesystem.selectors.best_candidate_selector import (
    BestCandidateSelector,
)


class FilesystemSearchEngine:

    def __init__(self):

        directories = UserDirectories()

        self.scanner = FileScanner()

        self.matcher = FileMatcher()

        self.ranker = FileRanker()

        self.selector = BestCandidateSelector()

        self.index = self.scanner.index(
            directories.documents(),
        )

    def search(
        self,
        query,
    ):

        matches = self.matcher.search(
            query,
            self.index,
        )

        candidates = self.ranker.rank(
            matches,
        )

        return self.selector.select(
            candidates,
        )
