from pathlib import Path
import subprocess
# import webbrowser

from jarvis.platforms.base import Platform


class LinuxPlatform(Platform):

    def open_application(self, executable: str) -> bool:
        try:
            subprocess.Popen(
                [executable],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
            )
            return True
        except Exception:
            return False

    def open_url(
        self,
        url: str,
        browser: str = "",
    ) -> bool:

        try:

            browser = browser.lower().strip()

            browsers = {

                "firefox": "firefox",

                "chrome": "google-chrome",

                "google": "google-chrome",

                "brave": "brave-browser",

                "edge": "microsoft-edge",

            }

            executable = browsers.get(browser)

            if executable:

                subprocess.Popen(
                    [executable, url],
                    stdout=subprocess.DEVNULL,
                    stderr=subprocess.DEVNULL,
                )

            else:

                subprocess.Popen(
                    ["xdg-open", url],
                    stdout=subprocess.DEVNULL,
                    stderr=subprocess.DEVNULL,
                )

            return True

        except Exception:

            return False

    def open_folder(self, path: str) -> bool:
        try:
            path = str(Path(path).expanduser())
            subprocess.Popen(
                ["xdg-open", path],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
            )
            return True
        except Exception:
            return False

    def open_file(self, path: str) -> bool:
        try:
            path = str(Path(path).expanduser())
            subprocess.Popen(
                ["xdg-open", path],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
            )
            return True
        except Exception:
            return False
