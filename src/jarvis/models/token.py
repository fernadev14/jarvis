from pydantic import BaseModel

from jarvis.models.token_kind import TokenKind


class Token(BaseModel):

    text: str

    normalized: str

    index: int

    kind: TokenKind = TokenKind.UNKNOWN
