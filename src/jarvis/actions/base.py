from abc import ABC, abstractmethod

from jarvis.core.intent import Intent
from jarvis.models.action_request import ActionRequest
from jarvis.models.action_result import ActionResult


class Action(ABC):

    @property
    @abstractmethod
    def intent(self) -> Intent:
        """Intención que maneja esta acción."""
        ...

    @abstractmethod
    def execute(self, request: ActionRequest) -> ActionResult:
        """Ejecuta la acción."""
        ...
