from jarvis.nlu.text_preprocessor import TextPreprocessor
from jarvis.nlu.tokenizer import Tokenizer
from jarvis.nlu.sentence_parser import SentenceParser

preprocessor = TextPreprocessor()
tokenizer = Tokenizer()
parser = SentenceParser()

tests = [
    "abre firefox",
    "abreme firefox",
    "puedes abrir firefox",
    "quiero abrir github",
    "hola",
]

for text in tests:

    print("-" * 40)

    print(text)

    text = preprocessor.preprocess(text)

    tokens = tokenizer.tokenize(text)

    sentence = parser.parse(tokens)

    print(sentence)
