from dataclasses import dataclass, field


@dataclass
class InstalledApplication:

    name: str

    executable: str

    desktop_file: str

    icon: str = ""

    categories: list[str] = field(default_factory=list)

    aliases: list[str] = field(default_factory=list)
