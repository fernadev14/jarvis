from jarvis.nlu.entity_normalizer import EntityNormalizer

normalizer = EntityNormalizer()

tests = [
    "el contrato",
    "la factura",
    "mi contrato",
    "el proyecto jarvis",
    "unas imagenes",
    "la carpeta musica",
    "el archivo contrato",
    "el documento contrato",
    "la aplicacion firefox",
    "la página github",
]

for test in tests:

    print("-" * 40)
    print(test)
    print(normalizer.normalize(test))
