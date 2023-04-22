from pydantic import BaseModel


class CharacterModel(BaseModel):
    description: str
    