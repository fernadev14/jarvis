from dataclasses import dataclass, field


@dataclass
class SearchItem:

    resource_id: str

    name: str

    aliases: list[str] = field(default_factory=list)

    score: float = 0.0
