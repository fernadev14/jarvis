from pathlib import Path


class UserDirsParser:

    FILE = Path.home() / ".config" / "user-dirs.dirs"

    def load(self):

        result = {}

        if not self.FILE.exists():
            return result

        for line in self.FILE.read_text().splitlines():

            line = line.strip()

            if not line:

                continue

            if line.startswith("#"):

                continue

            if "=" not in line:

                continue

            key, value = line.split("=", 1)

            value = value.strip().strip('"')

            value = value.replace("$HOME", str(Path.home()))

            result[key] = value

        return result
