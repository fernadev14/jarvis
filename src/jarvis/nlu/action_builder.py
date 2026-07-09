from jarvis.models.action import Action


class ActionBuilder:

    def build(self, sentence):

        return Action(

            intent=sentence.intent,

            target=sentence.target,

            context=sentence.context,

            tool=sentence.tool,

            location=sentence.location,

            modifiers=sentence.modifiers,
        )
