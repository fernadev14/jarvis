import subprocess
# import webbrowser

from jarvis.platforms.base import Platform


class MacOSPlatform(Platform):

    def open_application(self, executable: str) -> bool:
        try:
            subprocess.Popen(
                ["open", "-a", executable],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
            )
            return True
        except Exception:
            return False

    def open_url(self, url: str) -> bool:
        try:
            subprocess.Popen(
                ["open", url],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
            )
            return True
        except Exception:
            return False

    def open_folder(self, path: str) -> bool:
        try:
            subprocess.Popen(
                ["open", path],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
            )
            return True
        except Exception:
            return False

    def open_file(self, path: str) -> bool:
        try:
            subprocess.Popen(
                ["open", path],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
            )
            return True
        except Exception:
            return False
