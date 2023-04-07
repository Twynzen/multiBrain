class Character:
    description: str
    id: int

    def __init__(self, description, id) -> None:
        self.description = description
        self.id = id

    def create(self, description):
        pass
