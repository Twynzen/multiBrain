from database import Database


class CharacterService():
    id: str
    description: str

    def __init__(self, description) -> None:
        self.description = description

    def create(self):
        print(self.description)
        connection = Database.get_connection()
        print(connection)
        # database = self.client_database.multibrain
        # collection_characters = database.characters
