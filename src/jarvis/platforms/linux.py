import shutil
import subprocess

from jarvis.platforms.base import Platform


class LinuxPlatform(Platform):

    def open_application(self, app: str) -> bool:

        executable = shutil.which(app)

        if executable is None:
            return False

        subprocess.Popen([executable])

        return True

    def shutdown(self) -> bool:

        return False

    def restart(self) -> bool:

        return False
