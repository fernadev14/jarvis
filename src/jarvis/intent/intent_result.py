from dataclasses import dataclass

from jarvis.models.resource import Resource


@dataclass(slots=True)
class IntentResult:

    success: bool

    message: str

    resource: Resource | None = None
