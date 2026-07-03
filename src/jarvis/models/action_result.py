from pydantic import BaseModel


class ActionResult(BaseModel):

    success: bool

    message: str

    data: dict = {}
