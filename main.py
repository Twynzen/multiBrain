from fastapi import FastAPI
from router import character
from models import Database
import asyncio

async def prerequisites():
    connection = Database()
    result = await connection.connect_to_the_database()
    print(result)

prerequisites()

app = FastAPI()
app.include_router(character.router, prefix="/api/v1")

""" Test endpoints """


@app.get("/home", status_code=200)
def read_root():
    return {"Hello": "World"}

if __name__ == "__main__":
    asyncio.run(prerequisites())