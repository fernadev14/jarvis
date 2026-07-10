import platform

from jarvis.platforms.discovery.linux_repository import (
    LinuxRepository,
)


class DiscoveryFactory:

    @staticmethod
    def create():

        system = platform.system()

        if system == "Linux":

            return LinuxRepository()

        raise RuntimeError(
            f"{system} todavía no soportado."
        )
