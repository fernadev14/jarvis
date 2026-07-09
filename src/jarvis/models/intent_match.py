from pydantic import BaseModel


class IntentMatch(BaseModel):

    intent: str

    verb: str

    verb_index: int
