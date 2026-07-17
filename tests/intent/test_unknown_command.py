from jarvis.intent.intent_engine import (
    IntentEngine,
)


engine = IntentEngine()

result = engine.execute(
    "hola jarvis",
)

print(result)

engine.stop()
