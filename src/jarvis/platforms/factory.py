import platform

from jarvis.platforms.linux import LinuxPlatform
from jarvis.platforms.windows import WindowsPlatform
from jarvis.platforms.macos import MacOSPlatform


class PlatformFactory:

    @staticmethod
    def create():

        system = platform.system()

        if system == "Linux":
            return LinuxPlatform()

        if system == "Windows":
            return WindowsPlatform()

        if system == "Darwin":
            return MacOSPlatform()

        raise RuntimeError(f"Sistema operativo no soportado: {system}")
