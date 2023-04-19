from pydantic import BaseModel


class Character(BaseModel):
    id: str
    description: str

    def __init__(self, **data) -> None:
        super().__init__(**data)
        self.id = self.id.upper()
        self.description = self.description.upper()

    def create(self, description):
        pass
