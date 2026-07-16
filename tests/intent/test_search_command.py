from jarvis.intent.intent_engine import (
    IntentEngine,
)


engine = IntentEngine()

result = engine.execute(
    "busca firefox",
)

print(result)

engine.stop()
