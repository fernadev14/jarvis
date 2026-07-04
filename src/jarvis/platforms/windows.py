import os
# import webbrowser

from jarvis.platforms.base import Platform


class WindowsPlatform(Platform):

    def open_application(self, executable: str) -> bool:
        try:
            os.startfile(executable)
            return True
        except Exception:
            return False

    def open_url(self, url: str) -> bool:
        import os
        try:
            os.startfile(url)
            return True
        except Exception:
            return False

    def open_folder(self, path: str) -> bool:
        try:
            os.startfile(path)
            return True
        except Exception:
            return False

    def open_file(self, path: str) -> bool:
        try:
            os.startfile(path)
            return True
        except Exception:
            return False
