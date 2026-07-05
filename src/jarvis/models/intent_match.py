from pydantic import BaseModel


class IntentMatch(BaseModel):

    intent: str

    pattern: str

    start: int

    end: int
