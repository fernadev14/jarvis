from pydantic import BaseModel

from jarvis.core.intent import Intent


class ActionRequest(BaseModel):

    intent: Intent

    text: str

    entity: str
