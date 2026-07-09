from jarvis.nlu.intent_detector import IntentDetector
from jarvis.nlu.tokenizer import Tokenizer

detector = IntentDetector()
tokenizer = Tokenizer()

tests = [
    "abre firefox",
    "abreme firefox",
    "abrir firefox",
    "abrirme firefox",
    "hola",
    "buenas",
    "hey",
    "puedes abrir firefox",
    "podrias abrir mysql",
    "quiero abrir youtube",
    "necesito abrir google",
    "me ayudas a abrir github",
    "puedes abrir github",
]

for text in tests:

    print("-" * 40)

    print(text)

    tokens = tokenizer.tokenize(text)

    print(tokens)

    print(detector.detect(tokens))
