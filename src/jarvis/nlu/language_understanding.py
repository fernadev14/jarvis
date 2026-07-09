from jarvis.models.resource_type import ResourceType
# from jarvis.nlu.entity_extractor import EntityExtractor
from jarvis.nlu.entity_normalizer import EntityNormalizer
from jarvis.nlu.entity_resolver import EntityResolver
# from jarvis.nlu.intent_detector import IntentDetector
from jarvis.nlu.text_preprocessor import TextPreprocessor
from jarvis.nlu.tokenizer import Tokenizer
from jarvis.nlu.understanding import Understanding
from jarvis.nlu.sentence_parser import SentenceParser


class LanguageUnderstanding:

    def __init__(self):

        self.text_preprocessor = TextPreprocessor()

        self.tokenizer = Tokenizer()

        self.parser = SentenceParser()

        # self.intent_detector = IntentDetector()

        # self.entity_extractor = EntityExtractor()

        self.entity_normalizer = EntityNormalizer()

        self.entity_resolver = EntityResolver()

    def understand(self, text: str) -> Understanding:

        text = self.text_preprocessor.preprocess(text)

        tokens = self.tokenizer.tokenize(text)

        sentence = self.parser.parse(tokens)

        entity = self.entity_normalizer.normalize(
            sentence.object,
        )

        resource = self.entity_resolver.resolve(entity)

        resource_type = (
            resource.resource_type
            if resource is not None
            else ResourceType.UNKNOWN
        )

        intent = "open"

        if sentence.verb in {
            "hola",
            "buenas",
            "hey",
        }:
            intent = "chat"

        return Understanding(
            intent=intent,
            entity=entity,
            resource_type=resource_type,
            resource=resource,
        )
