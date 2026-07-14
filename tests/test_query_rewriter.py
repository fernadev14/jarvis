from jarvis.search.rewriter.query_rewriter import QueryRewriter

rewriter = QueryRewriter()

queries = [

    "abre visual estudio code",

    "abre google chrome",

    "abre configuracion",

    "abre yotuve",

    "abre firefos",

    "abre la terminal de comandos",

    "abreme por favor visual estudio",

    "abreme el archivo que se llama contrato que esta dentro de documentos",

    "abre cv fernando que esta dentro de documentos",

]

for query in queries:

    print("-" * 40)

    print(query)

    print(rewriter.rewrite(query))
