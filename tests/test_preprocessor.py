from jarvis.nlu.text_preprocessor import TextPreprocessor

processor = TextPreprocessor()

tests = [
    "¿Podrías abrirme el contrato, por favor?",
    "¡¡ABRE FIREFOX!!",
    "Árbol",
    "   Hola     Mundo   ",
    "Música",
    "GitHub.",
]

for test in tests:

    print("-" * 40)
    print(test)
    print(processor.preprocess(test))
