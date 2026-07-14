from jarvis.search.filesystem.matcher import FileMatcher
from jarvis.search.filesystem.ranking.file_ranker import FileRanker
from jarvis.search.filesystem.scanner import FileScanner
from jarvis.platforms.userdirs.user_directories import UserDirectories

directories = UserDirectories()

scanner = FileScanner()

index = scanner.index(
    directories.documents()
)

matcher = FileMatcher()

ranker = FileRanker()

matches = matcher.search(
    "contrato",
    index,
)

results = ranker.rank(matches)

for candidate in results[:10]:
    print(candidate.score, candidate.record.name)
