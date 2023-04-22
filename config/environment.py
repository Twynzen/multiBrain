from dotenv import load_dotenv
import os

load_dotenv()

""" Database environment """
_user_database = os.getenv("MONGODB_USER")
_password_database = os.getenv("MONGODB_PASS")
_host_database = os.getenv("MONGODB_HOST")
_port_database = os.getenv("MONGODB_PORT")
MONGO_URI_DATABASE = f'mongodb://{_user_database}:{_password_database}@{_host_database}:{_port_database}/'
