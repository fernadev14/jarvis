from pathlib import Path

from rapidfuzz import fuzz, process

from jarvis.platforms.discovery.base import DiscoveryRepository
from jarvis.platforms.discovery.linux_desktop_parser import (
    LinuxDesktopParser,
)


class LinuxRepository(DiscoveryRepository):

    SEARCH_PATHS = [
        Path("/usr/share/applications"),
        Path("/usr/local/share/applications"),
        Path.home() / ".local/share/applications",
    ]

    def __init__(self):

        self.parser = LinuxDesktopParser()

        self.applications = []

        self.load()

    def load(self):

        self.applications.clear()

        for folder in self.SEARCH_PATHS:

            if not folder.exists():
                continue

            for file in folder.glob("*.desktop"):

                app = self.parser.parse(file)

                if app:

                    self.applications.append(app)

    def find(self, text):

        if not text:

            return None

        text = text.lower().strip()

        #
        # 1. Buscar coincidencia exacta
        #

        for app in self.applications:

            if app.name.lower() == text:

                return app

            if text in app.aliases:

                return app

        #
        # 2. Buscar por similitud
        #

        candidates = {}

        for app in self.applications:

            candidates[app.name.lower()] = app

            for alias in app.aliases:

                candidates[alias.lower()] = app

        result = process.extractOne(
            text,
            candidates.keys(),
            scorer=fuzz.WRatio,
        )

        if result is None:

            return None

        match, score, _ = result

        if score < 80:

            return None

        return candidates[match]
