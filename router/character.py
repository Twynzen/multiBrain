import models
from fastapi import APIRouter

router = APIRouter()


@router.get("/characters/", tags=["users"])
async def get_character():
    return f"Get test"


@router.get("/characters/{id}", tags=["users"])
async def get_character_by_id(id):
    return f"Get test by id: {id}"


@router.post("/characters/", tags=["users"])
async def post_character(character: models.CharacterModel):
    character.create();
