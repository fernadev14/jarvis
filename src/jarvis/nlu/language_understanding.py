from jarvis.nlu.intent_detector import IntentDetector
from jarvis.nlu.entity_extractor import EntityExtractor
from jarvis.nlu.entity_resolver import EntityResolver
from jarvis.nlu.understanding import Understanding
from jarvis.models.resource_type import ResourceType
from jarvis.nlu.entity_normalizer import EntityNormalizer
from jarvis.nlu.text_preprocessor import TextPreprocessor
from jarvis.models.intent_match import IntentMatch


class EntityExtractor:
    def extract(
        self,
        text: str,
        match: IntentMatch,
    ) -> str:
        return text[match.end:].strip()


class LanguageUnderstanding:

    def __init__(self):

        self.text_preprocessor = TextPreprocessor()

        self.intent_detector = IntentDetector()

        self.entity_extractor = EntityExtractor()

        self.entity_normalizer = EntityNormalizer()

        self.entity_resolver = EntityResolver()

    def understand(self, text: str) -> Understanding:

        text = self.text_preprocessor.preprocess(text)

        intent_match = self.intent_detector.detect(text)

        entity = self.entity_extractor.extract(
            text,
            intent_match,
        )

        entity = self.entity_normalizer.normalize(entity)

        resource = self.entity_resolver.resolve(entity)

        resource_type = (
            resource.resource_type
            if resource is not None
            else ResourceType.UNKNOWN
        )

        return Understanding(
            intent=intent_match.intent,
            entity=entity,
            resource_type=resource_type,
            resource=resource,
        )
