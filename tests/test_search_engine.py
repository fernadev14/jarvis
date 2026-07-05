from jarvis.files.search_engine import SearchEngine

engine = SearchEngine()

tests = [

    "contrato",

    "factura",

    "imagen",

    "jarvis",

]

for test in tests:

    print("-" * 40)

    print(test)

    print(engine.search(test))
