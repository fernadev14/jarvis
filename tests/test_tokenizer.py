from jarvis.nlu.tokenizer import Tokenizer

tokenizer = Tokenizer()

tests = [
    "abre firefox",
    "puedes abrir github",
    "hola jarvis",
]

for text in tests:

    print("-" * 40)

    print(text)

    tokens = tokenizer.tokenize(text)

    for token in tokens:
        print(token)
