from database import Database


class CharacterService():
    id: str
    description: str

    def __init__(self, description) -> None:
        self.description = description

    def create(self):
        print(self.description)
        connection = Database.get_connection()
        database = connection.multibrain
        collection_characters = database.characters
        result = collection_characters.insert_one(self.description)
        return result
