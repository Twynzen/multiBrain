from fastapi import FastAPI, APIRouter

router = APIRouter()


@router.get("/characters/", tags=["users"])
async def get_character():
  return f"Get test"

@router.get("/characters/{id}", tags=["users"])
async def get_character_by_id(id):
  return f"Get test by id: {id}"

@router.post("/characters/{description}", tags=["users"])
async def post_character():
  return f"Post test"