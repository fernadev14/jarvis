class IgnoreRules:

    DIRECTORIES = {

        ".git",

        ".cache",

        "__pycache__",

        ".venv",

        "node_modules",

        "dist",

        "build",

        "target",

        ".idea",

        ".vscode",

        ".snap",

    }

    def ignore(self, path):

        return path.name in self.DIRECTORIES
