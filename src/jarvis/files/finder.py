from pathlib import Path


class FileFinder:

    def __init__(self):

        self.search_paths = [
            Path.home() / "Documents",
            Path.home() / "Downloads",
            Path.home() / "Desktop",
        ]

    def find(self, filename: str) -> Path | None:

        filename = filename.lower().strip()

        for directory in self.search_paths:

            if not directory.exists():
                continue

            for file in directory.rglob("*"):

                if not file.is_file():
                    continue

                if file.name.lower() == filename:

                    return file

        return None
