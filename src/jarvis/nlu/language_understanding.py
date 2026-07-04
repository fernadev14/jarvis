from jarvis.nlu.intent_detector import IntentDetector
from jarvis.nlu.entity_extractor import EntityExtractor
from jarvis.nlu.entity_resolver import EntityResolver
from jarvis.nlu.understanding import Understanding
from jarvis.models.resource_type import ResourceType


class LanguageUnderstanding:

    def __init__(self):

        self.intent_detector = IntentDetector()

        self.entity_extractor = EntityExtractor()

        self.entity_resolver = EntityResolver()

    def understand(self, text: str) -> Understanding:

        intent = self.intent_detector.detect(text)

        entity = self.entity_extractor.extract(text)

        resource = self.entity_resolver.resolve(entity)

        resource_type = (
            resource.resource_type
            if resource is not None
            else ResourceType.UNKNOWN
        )

        return Understanding(
            intent=intent,
            entity=entity,
            resource_type=resource_type,
            resource=resource,
        )
