from jarvis.intent.intent_engine import (
    IntentEngine,
)

engine = IntentEngine()

examples = [

    "   ÁBRÉME      FIREFOX",

    "EjEcÚTaMe      CHROME",

    "Ábrelo    Visual     Studio     Code",

    "   LANZAME      GIMP",

]

for text in examples:

    print("-" * 40)

    print("Entrada :", repr(text))

    result = engine.execute(
        text,
    )

    print(result)

engine.stop()
