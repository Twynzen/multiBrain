from dotenv import load_dotenv
import os

load_dotenv()

""" Database environment """
_user = os.getenv("MONGODB_USER")
_password = os.getenv("MONGODB_PASS")
_host = os.getenv("MONGODB_HOST")
_port = os.getenv("MONGODB_PORT")
MONGO_URI_DATABASE = f'mongodb://{_user}:{_password}@{_host}:{_port}/'
