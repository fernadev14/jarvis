from jarvis.platforms.base import Platform


class MacOSPlatform(Platform):

    def open_application(self, app: str) -> bool:
        raise NotImplementedError()

    def shutdown(self) -> bool:
        raise NotImplementedError()

    def restart(self) -> bool:
        raise NotImplementedError()
