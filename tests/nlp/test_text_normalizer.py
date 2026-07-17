from jarvis.nlp.text_normalizer import (
    TextNormalizer,
)

normalizer = TextNormalizer()

examples = [

    "   ÁBRÉME      FIREFOX",

    "EjEcÚTaMe      CHROME",

    "Ábrelo    Visual     Studio     Code",

    "   LANZAME      GIMP",

]

for text in examples:

    print("ANTES :", repr(text))

    print(
        "DESPUÉS:",
        repr(
            normalizer.normalize(
                text,
            )
        )
    )

    print()
