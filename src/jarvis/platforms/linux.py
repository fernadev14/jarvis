import shutil
import subprocess

from jarvis.platforms.base import Platform


class LinuxPlatform(Platform):

    def open_application(self, executable: str) -> bool:

        path = shutil.which(executable)

        if path is None:
            return False

        subprocess.Popen(
            [path],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )

        return True

    def open_url(self, url: str) -> bool:

        opener = shutil.which("xdg-open")

        if opener is None:
            return False

        subprocess.Popen(
            [opener, url],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )

        return True
