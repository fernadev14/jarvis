from jarvis.platforms.userdirs.user_directories import (
    UserDirectories,
)

from jarvis.search.filesystem.matcher import (
    FileMatcher,
)

from jarvis.search.filesystem.scanner import (
    FileScanner,
)

scanner = FileScanner()

dirs = UserDirectories()

index = scanner.index(
    dirs.documents(),
)

matcher = FileMatcher()

queries = [

    "contrato",

    "certificado laboral",

    "registro civil",

    "foto",

    "tarjeta",

    "pension",

    "softwareone",

]

for query in queries:

    print()

    print("=" * 60)

    print(query)

    print("=" * 60)

    results = matcher.search(
        query,
        index,
    )

    for score, record in results[:5]:

        print(

            round(score, 1),

            record.name,

        )
