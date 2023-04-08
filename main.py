from fastapi import FastAPI
from typing import Union
from router import character

app = FastAPI()
app.include_router(character.router, prefix="/api/v1")

""" Test endpoints """
@app.get("/home", status_code=200)
def read_root():
  return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
  return {"item_id": item_id, "q": q}
