from pydantic import BaseModel


class Attributes(BaseModel):
    image: str
    name: str
