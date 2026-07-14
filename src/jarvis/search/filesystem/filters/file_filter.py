from pathlib import Path


class FileFilter:

    ALLOWED_EXTENSIONS = {

        ".pdf",

        ".doc",

        ".docx",

        ".txt",

        ".md",

        ".odt",

        ".rtf",

        ".xls",

        ".xlsx",

        ".csv",

        ".ppt",

        ".pptx",

        ".png",

        ".jpg",

        ".jpeg",

        ".gif",

        ".webp",

        ".mp3",

        ".wav",

        ".ogg",

        ".flac",

        ".mp4",

        ".mkv",

        ".avi",

        ".zip",

        ".rar",

        ".7z",

        ".tar",

        ".gz",

    }

    def allow(
        self,
        path: Path,
    ) -> bool:

        return path.suffix.lower() in self.ALLOWED_EXTENSIONS
