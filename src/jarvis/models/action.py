from dataclasses import dataclass, field


@dataclass
class Action:

    intent: str

    target: str

    context: str = ""

    tool: str = ""

    location: str = ""

    modifiers: list[str] = field(default_factory=list)
