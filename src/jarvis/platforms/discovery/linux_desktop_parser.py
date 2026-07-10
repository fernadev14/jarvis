from configparser import ConfigParser
from pathlib import Path

from jarvis.platforms.discovery.application import InstalledApplication


class LinuxDesktopParser:

    def parse(self, file: Path):

        parser = ConfigParser(interpolation=None)

        parser.read(file, encoding="utf-8")

        if "Desktop Entry" not in parser:

            return None

        entry = parser["Desktop Entry"]

        name = entry.get("Name", "")

        executable = entry.get("Exec", "").strip()

        if not executable:
            return None

        parts = executable.split()

        if not parts:
            return None

        executable = parts[0]

        icon = entry.get("Icon", "")

        categories = entry.get(
            "Categories",
            "",
        ).split(";")

        aliases = self.build_aliases(name)

        return InstalledApplication(

            name=name,

            executable=executable,

            desktop_file=str(file),

            icon=icon,

            categories=categories,

            aliases=aliases,
        )

    def build_aliases(self, name):

        name = name.lower()

        aliases = {
            name,
        }

        words = name.split()

        aliases.update(words)

        return sorted(aliases)
