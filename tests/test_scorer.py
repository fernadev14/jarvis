from jarvis.files.scorer import Scorer


scorer = Scorer()

tests = [

    ("contrato", "contrato.pdf"),

    ("contrato", "contrato_cliente.pdf"),

    ("contrato", "imagen.png"),

    ("factura", "factura.xlsx"),

    ("jarvis", "jarvis-ai"),

]

for query, candidate in tests:

    print("-" * 40)

    print(query)

    print(candidate)

    print(
        scorer.score(
            query,
            candidate,
        )
    )
