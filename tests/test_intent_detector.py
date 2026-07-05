from jarvis.nlu.intent_detector import IntentDetector

detector = IntentDetector()

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
]

for test in tests:

    print("-" * 40)
    print(test)
    result = detector.detect(test)
    print(result)
