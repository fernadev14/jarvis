from jarvis.search.search import SearchEngine

engine = SearchEngine()

queries = [

    "visual estudio code",

    "visul studio",

    "firesfox",

    "chrom",

    "goog",

    "gpart",

    "software y actualizaciones",

]

for query in queries:

    print("-" * 40)

    print(query)

    results = engine.search(query)

    if results:

        print(results[0])
