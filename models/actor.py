from pydantic import BaseModel, Field

from models.attributes import Attributes


class Actor(BaseModel):
    id: str = Field(..., validation_alias="ID")
    attributes: Attributes = Field(..., validation_alias="Attributes")
