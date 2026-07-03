from jarvis.nlu.intent_detector import IntentDetector
from jarvis.nlu.entity_extractor import EntityExtractor
from jarvis.nlu.entity_resolver import EntityResolver
from jarvis.nlu.understanding import Understanding


class LanguageUnderstanding:

    def __init__(self):

        self.intent_detector = IntentDetector()

        self.entity_extractor = EntityExtractor()

        self.entity_resolver = EntityResolver()

    def understand(self, text: str):

        intent = self.intent_detector.detect(text)

        entity = self.entity_extractor.extract(text)

        entity_type = self.entity_resolver.resolve(entity)

        return Understanding(
            intent=intent,
            entity=entity,
            entity_type=entity_type,
        )
