from jarvis.intent.intent_engine import (
    IntentEngine,
)


engine = IntentEngine()

result = engine.execute(
    "abre firefox",
)

print(result)

engine.stop()
