from yaml import tokens

from jarvis.models.resource_type import ResourceType

from jarvis.nlu.text_preprocessor import TextPreprocessor
from jarvis.nlu.tokenizer import Tokenizer
from jarvis.nlu.token_classifier import TokenClassifier
from jarvis.nlu.sentence_parser import SentenceParser
from jarvis.nlu.query_cleaner import QueryCleaner
from jarvis.nlu.entity_extractor import EntityExtractor
from jarvis.nlu.action_builder import ActionBuilder
from jarvis.nlu.entity_normalizer import EntityNormalizer
from jarvis.nlu.understanding import Understanding
from jarvis.search.search import SearchEngine

from jarvis.platforms.browser_normalizer import BrowserNormalizer


class Pipeline:

    def __init__(self):

        self.preprocessor = TextPreprocessor()

        self.tokenizer = Tokenizer()

        self.classifier = TokenClassifier()

        self.parser = SentenceParser()

        self.cleaner = QueryCleaner()

        self.entity_extractor = EntityExtractor()

        self.action_builder = ActionBuilder()

        self.normalizer = EntityNormalizer()

        self.browser_normalizer = BrowserNormalizer()

        self.search = SearchEngine()

    def run(self, text: str) -> Understanding:

        text = self.preprocessor.preprocess(text)

        tokens = self.tokenizer.tokenize(text)

        tokens = self.classifier.classify(tokens)

        sentence = self.parser.parse(tokens)

        tokens = self.cleaner.clean(tokens)

        entities = self.entity_extractor.extract(tokens)

        entities = self.entity_extractor.extract(tokens)

        sentence.target = entities["target"]
        sentence.tool = entities["tool"]
        sentence.location = entities["location"]

        action = self.action_builder.build(sentence)

        action.target = self.normalizer.normalize(
            action.target,
        )

        action.tool = self.browser_normalizer.normalize(
            action.tool,
        )

        resource = self.search.resolve(
            action.target,
        )

        resource_type = (
            resource.resource_type
            if resource is not None
            else ResourceType.UNKNOWN
        )

        print(action)

        return Understanding(
            intent=action.intent,
            entity=action.target,
            context=action.context,
            tool=action.tool,
            location=action.location,
            resource_type=resource_type,
            resource=resource,
        )
