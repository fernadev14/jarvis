from jarvis.nlu.text_preprocessor import TextPreprocessor
from jarvis.nlu.tokenizer import Tokenizer
from jarvis.nlu.token_classifier import TokenClassifier

preprocessor = TextPreprocessor()
tokenizer = Tokenizer()
classifier = TokenClassifier()

tests = [
    "abre firefox",
    "puedes abrir github",
    "firefox lo puedes abrir",
    "por favor abre documentos",
    "abre la aplicacion firefox",
    "abre la carpeta descargas",
    "abre el archivo contrato",
    "abre github en brave",
    "abre youtube con firefox",
    "el archivo llamado contrato",
]

for text in tests:

    print("-" * 40)

    print(text)

    text = preprocessor.preprocess(text)

    tokens = tokenizer.tokenize(text)

    tokens = classifier.classify(tokens)

    for token in tokens:
        print(token)
