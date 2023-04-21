from fastapi import FastAPI
from router import character
from models import Database
import asyncio

connection = Database()
app = FastAPI()
app.include_router(character.router, prefix="/api/v1")

""" Test endpoints """


@app.get("/home", status_code=200)
def read_root():
    return {"Hello": "World"}

if __name__ == "__main__":
    pass