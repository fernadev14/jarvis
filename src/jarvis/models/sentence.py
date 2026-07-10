from dataclasses import dataclass, field


@dataclass
class Sentence:

    intent: str

    verb: str

    target: str

    context: str = ""

    tool: str = ""

    location: str = ""

    modifiers: list[str] = field(default_factory=list)

    target_tokens: list[str] = field(default_factory=list)
