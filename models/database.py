from motor.motor_asyncio import AsyncIOMotorClient
from config import DatabaseEnvironment


class Database:
    user: str
    password: str
    host: str
    port: int

    def __init__(self):
        database_info = DatabaseEnvironment()
        self.user = database_info.user
        self.password = database_info.password
        self.host = database_info.host
        self.port = database_info.port

    async def connect_to_the_database(self):
        client = AsyncIOMotorClient(
            f'mongodb://{self.user}:{self.password}@{self.host}:{self.port}/')
        db = client["MultiBrain"]
        return db
