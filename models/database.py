# from motor.motor_asyncio import AsyncIOMotorClient
from pymongo import MongoClient
from config import DatabaseEnvironment
from helpers import write_info_in_a_log


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
        self.__connect_to_the_database()

    def __connect_to_the_database(self):
        database_log_file = 'database'
        MONGO_URI_DATABASE = f'mongodb://{self.user}:{self.password}@{self.host}:{self.port}/'
        client = MongoClient(MONGO_URI_DATABASE)
        write_info_in_a_log(
            'Conected successfully to the database, list of available databases:', database_log_file)
        for database in client.list_database_names():
            write_info_in_a_log(database, database_log_file)
