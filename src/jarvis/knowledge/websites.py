from pathlib import Path

import yaml


class WebsiteRegistry:

    def __init__(self):

        self.websites = {}

        self.load()

    def load(self):

        file = (
            Path(__file__).parent
            / "websites.yml"
        )

        with open(file, "r", encoding="utf8") as f:

            self.websites = yaml.safe_load(f)

    def find(self, text: str):

        text = text.lower()

        for name, info in self.websites.items():

            if text == name:
                return info

            if text in info["aliases"]:
                return info

        return None
