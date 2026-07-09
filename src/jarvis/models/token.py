from pydantic import BaseModel


class Token(BaseModel):

    text: str

    normalized: str

    index: int
