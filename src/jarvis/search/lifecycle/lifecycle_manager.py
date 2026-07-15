class LifecycleManager:

    def __init__(self):

        self.providers = []

    def register(
        self,
        provider,
    ):

        for current in self.providers:

            if type(current) is type(provider):

                return

        self.providers.append(provider)

    def load(
        self,
        index,
        repository,
    ):

        for provider in self.providers:

            provider.load(
                index,
                repository,
            )
