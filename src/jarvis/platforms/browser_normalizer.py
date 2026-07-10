class BrowserNormalizer:

    BROWSERS = {

        "google": "google-chrome",
        "google chrome": "google-chrome",
        "chrome": "google-chrome",
        "google-chrome": "google-chrome",

        "firefox": "firefox",
        "mozilla": "firefox",

        "brave": "brave-browser",
        "brave browser": "brave-browser",
        "brave-browser": "brave-browser",

        "edge": "microsoft-edge",
        "microsoft edge": "microsoft-edge",
        "microsoft-edge": "microsoft-edge",
    }

    def normalize(self, browser: str) -> str:

        if not browser:
            return ""

        return self.BROWSERS.get(
            browser.lower(),
            browser.lower(),
        )
