from pymongo import MongoClient
from config import MONGO_URI_DATABASE
from helpers import Logs

""" AG: I'm using classmethod to avoid the use of singleton and keep only one connection """

class Database:
    user: str
    password: str
    host: str
    port: int
    client: MongoClient = None
    log = Logs()
    

    def __init__(self):
        self.__connect_to_the_database()

    @classmethod
    def list_databases(cls, print_databases: bool = False) -> None:
        cls.log.write_info_in_a_log('Listing the databases', 'database')
        for database in cls.client.list_database_names():
            cls.log.write_info_in_a_log(database, 'database')
            if (print_databases):
                print(database)

    """ AG: I created the connect to the database like a private method to avoid the creation
        of more than one connection to the database, the idea is to have only one
        connection to the database """
    @classmethod
    def __connect_to_the_database(cls) -> None:

        try:
            client = MongoClient(MONGO_URI_DATABASE)
            cls.client = client
            cls.log.write_info_in_a_log(
                'Conected successfully to the database', 'database')
            cls.list_databases()
            return client
        except (Exception) as e:
            print(
                f'Unexpected error with the database model, please check the log')
            cls.log.write_error_in_a_log(e, 'database')

    @classmethod
    def get_connection(cls) -> MongoClient:
        if cls.client is None:
            print("Está en None")
            cls.client = MongoClient(MONGO_URI_DATABASE)
        return cls.client
