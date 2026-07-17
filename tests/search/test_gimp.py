from jarvis.search.search import SearchEngine

engine = SearchEngine()

queries = [

    "gimp",

    "gim",

    "gimp editor",

]

for query in queries:

    print("-" * 40)

    print(query)

    print(
        engine.search(
            query,
        )[:10]
    )

engine.stop()
