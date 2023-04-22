import models
from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder
from services import CharacterService

router = APIRouter()


@router.get("/characters/", tags=["users"])
async def get_character():
    return f"Get test"


@router.get("/characters/{id}", tags=["users"])
async def get_character_by_id(id):
    return f"Get test by id: {id}"


@router.post("/characters/", tags=["users"])
async def post_character(character_body: models.CharacterModel):
    character_dict = jsonable_encoder(character_body)
    print(type(character_dict))
    service = CharacterService(character_dict)
    return f'Status: {service.create()}'
