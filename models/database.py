# from motor.motor_asyncio import AsyncIOMotorClient
from pymongo import MongoClient
from config import MONGO_URI_DATABASE
from helpers import write_info_in_a_log


class Database:
    user: str
    password: str
    host: str
    port: int
    client: MongoClient

    def __init__(self):
        self.__connect_to_the_database()
        self.list_databases(self.client)

    def list_databases(self, client: MongoClient, print_databases: bool = False) -> None:
        write_info_in_a_log('Listing the databases', 'database')
        for database in client.list_database_names():
            write_info_in_a_log(database, 'database')
            if (print_databases):
                print(database)

    """ AG: I created the connect to the database like a private method to avoid the creation
        of more than one connection to the database, the idea is to have only one
        connection to the database """

    def __connect_to_the_database(self):
        try:
            client = MongoClient(MONGO_URI_DATABASE)
            self.client = client
            write_info_in_a_log(
                'Conected successfully to the database', 'database')
        except Exception as e:
            print(f'Unexpected error, details: ', e)
