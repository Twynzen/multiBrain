from pydantic import BaseModel
from models import database


class CharacterModel(BaseModel):
    id: str
    description: str
    