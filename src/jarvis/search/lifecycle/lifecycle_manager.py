class LifecycleManager:

    def load(
        self,
        providers,
        service,
    ):

        for provider in providers:
            provider.load(service)
