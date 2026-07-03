class ActionRegistry:

    def __init__(self):

        self.actions = {}

    def register(self, action):

        self.actions[action.intent] = action

    def get(self, intent):

        return self.actions.get(intent)
