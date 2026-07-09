from jarvis.models.resource_type import ResourceType

from jarvis.nlu.text_preprocessor import TextPreprocessor
from jarvis.nlu.tokenizer import Tokenizer
from jarvis.nlu.token_classifier import TokenClassifier
from jarvis.nlu.sentence_parser import SentenceParser
from jarvis.nlu.action_builder import ActionBuilder
from jarvis.nlu.context_extractor import ContextExtractor
from jarvis.nlu.entity_normalizer import EntityNormalizer
from jarvis.nlu.entity_resolver import EntityResolver
from jarvis.nlu.understanding import Understanding


class Pipeline:

    def __init__(self):

        self.preprocessor = TextPreprocessor()

        self.tokenizer = Tokenizer()

        self.classifier = TokenClassifier()

        self.parser = SentenceParser()

        self.action_builder = ActionBuilder()

        self.context_extractor = ContextExtractor()

        self.normalizer = EntityNormalizer()

        self.resolver = EntityResolver()

    def run(self, text: str) -> Understanding:

        text = self.preprocessor.preprocess(text)

        tokens = self.tokenizer.tokenize(text)

        tokens = self.classifier.classify(tokens)

        sentence = self.parser.parse(tokens)

        action = self.action_builder.build(sentence)

        info = self.context_extractor.extract(tokens)

        action.context = info["context"]
        action.tool = info["browser"]

        action.target = self.normalizer.normalize(
            action.target,
        )

        resource = self.resolver.resolve(
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
