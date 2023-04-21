from models import Database


class CharacterService():
    id: str
    description: str
    client_database = Database.get_connection()

    def __init__(self, **data) -> None:
        super().__init__(**data)
        self.id = self.id.upper()
        self.description = self.description.upper()

    def create(self, description):
        database = self.client_database.multibrain
        collection_characters = database.characters
