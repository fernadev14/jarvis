from jarvis.nlu.pipeline import Pipeline


class LanguageUnderstanding:

    def __init__(self):

        self.pipeline = Pipeline()

    def understand(self, text):

        return self.pipeline.run(text)
