from jarvis.intent.intent_engine import (
    IntentEngine,
)

engine = IntentEngine()

queries = [
    "abre firefox",
    "abrir firefox",
    "ejecuta firefox",
    "inicia firefox",
    "lanza firefox",
]

for query in queries:

    print(query)

    print(
        engine.execute(
            query,
        )
    )

engine.stop()
