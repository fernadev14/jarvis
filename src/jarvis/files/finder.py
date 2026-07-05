import os
from pathlib import Path


class FileFinder:

    IGNORED_DIRECTORIES = {
        ".git",
        ".venv",
        "venv",
        "__pycache__",
        "node_modules",
        ".idea",
        ".vscode",
        "dist",
        "build",
    }

    def __init__(self, search_paths: list[Path] | None = None):

        if search_paths is None:

            search_paths = [
                Path.home() / "Documents",
                Path.home() / "Downloads",
                Path.home() / "Desktop",
            ]

        self.search_paths = search_paths

    def find(self) -> list[Path]:

        results = []

        for root in self.search_paths:

            if not root.exists():
                continue

            for current_root, dirs, files in os.walk(root):

                dirs[:] = [
                    d
                    for d in dirs
                    if d not in self.IGNORED_DIRECTORIES
                ]

                for file in files:

                    results.append(
                        Path(current_root) / file
                    )

        return results
