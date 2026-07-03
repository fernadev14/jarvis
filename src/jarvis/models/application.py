from pydantic import BaseModel


class Application(BaseModel):
    name: str
    aliases: list[str]
    executable: str
