from jarvis.search.filesystem.search_engine import (
    FilesystemSearchEngine,
)


engine = FilesystemSearchEngine()


queries = [

    "contrato",

    "certificado laboral",

    "registro civil",

    "softwareone",

    "archivo inexistente",

]


for query in queries:

    print()
    print("=" * 60)
    print(query)
    print("=" * 60)

    result = engine.search(
        query,
    )

    if result is None:

        print("No encontrado")

        continue

    print("Score :", result.score)
    print("Nombre:", result.record.name)
    print("Ruta  :", result.record.path)
