from pydantic import BaseModel

from jarvis.models.token import Token


class Sentence(BaseModel):

    tokens: list[Token]

    verb: str = ""

    verb_index: int = -1

    object: str = ""

    modifiers: list[str] = []
