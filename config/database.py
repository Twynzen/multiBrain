from dotenv import load_dotenv
import os

load_dotenv()


class DatabaseEnvironment:
    user: str
    password: str
    host: str
    port: int

    def __init__(self):
        self.user = os.getenv("MONGODB_USER")
        self.password = os.getenv("MONGODB_PASS")
        self.host = os.getenv("MONGODB_HOST")
        self.port = os.getenv("MONGODB_PORT")
        print(self)

    def __str__(self) -> str:
        return f"user: {self.user}\npassword: {self.password}\nhost: {self.host}\nport: {self.port}\n"
