from pathlib import Path

from .parser import UserDirsParser


class UserDirectories:

    def __init__(self):

        self.data = UserDirsParser().load()

    def desktop(self):

        return self._directory(
            "XDG_DESKTOP_DIR",
            "Desktop",
        )

    def documents(self):

        return self._directory(
            "XDG_DOCUMENTS_DIR",
            "Documents",
        )

    def downloads(self):

        return self._directory(
            "XDG_DOWNLOAD_DIR",
            "Downloads",
        )

    def music(self):

        return self._directory(
            "XDG_MUSIC_DIR",
            "Music",
        )

    def pictures(self):

        return self._directory(
            "XDG_PICTURES_DIR",
            "Pictures",
        )

    def videos(self):

        return self._directory(
            "XDG_VIDEOS_DIR",
            "Videos",
        )

    def public(self):

        return self._directory(
            "XDG_PUBLICSHARE_DIR",
            "Public",
        )

    def templates(self):

        return self._directory(
            "XDG_TEMPLATES_DIR",
            "Templates",
        )

    def _directory(
        self,
        key,
        fallback,
    ):

        if key in self.data:

            return Path(self.data[key])

        return Path.home() / fallback
