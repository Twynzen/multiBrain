from fastapi import FastAPI
from router import character
from models import Database
from helpers import Logs
try:
    connection = Database()
except Exception as e:
    print(e)
    log = Logs()
    print(
        f'Unexpected error, is not possible to connect to the database, please check the log')
    log.write_error_in_a_log(e, 'database')
app = FastAPI()
app.include_router(character.router, prefix="/api/v1")

""" Test endpoints """


@app.get("/home", status_code=200)
def read_root():
    return {"Hello": "World"}


if __name__ == "__main__":
    pass
