from jarvis.platforms.userdirs.user_directories import (
    UserDirectories,
)

from jarvis.search.filesystem.scanner import (
    FileScanner,
)

from jarvis.search.filesystem.matcher import (
    FileMatcher,
)

from jarvis.search.filesystem.ranking.file_ranker import (
    FileRanker,
)

from jarvis.search.filesystem.selectors.best_candidate_selector import (
    BestCandidateSelector,
)


directories = UserDirectories()

scanner = FileScanner()

index = scanner.index(
    directories.documents(),
)

matcher = FileMatcher()

ranker = FileRanker()

selector = BestCandidateSelector()


queries = [

    "contrato",

    "certificado laboral",

    "registro civil",

    "tarjeta",

    "softwareone",

    "archivo que no existe",

]


for query in queries:

    print()
    print("=" * 60)
    print(query)
    print("=" * 60)

    matches = matcher.search(
        query,
        index,
    )

    candidates = ranker.rank(
        matches,
    )

    best = selector.select(
        candidates,
    )

    if best is None:

        print("No encontrado")

        continue

    print("Score :", best.score)
    print("Nombre:", best.record.name)
    print("Ruta  :", best.record.path)
