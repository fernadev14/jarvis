from pathlib import Path

import yaml

from jarvis.models.application import Application


class ApplicationRegistry:

    def __init__(self):

        self.apps = {}

        self.load()

    def load(self):

        file = (
            Path(__file__)
            .parent
            / "applications.yml"
        )

        with open(file, "r", encoding="utf8") as f:

            data = yaml.safe_load(f)

        for name, info in data.items():

            app = Application(
                name=name,
                aliases=info["aliases"],
                executable=info["executable"]["linux"]
            )

            self.apps[name] = app

    def find(self, text: str):

        text = text.lower()

        for app in self.apps.values():

            if text == app.name:
                return app

            if text in app.aliases:
                return app

        return None
