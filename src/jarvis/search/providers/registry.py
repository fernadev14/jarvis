class ProviderRegistry:

    def __init__(self):

        self._providers = []

    def register(
        self,
        provider,
    ):

        for current in self._providers:

            if type(current) is type(provider):
                return

        self._providers.append(provider)

    def providers(self):

        return self._providers
