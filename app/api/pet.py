import json

from fastapi import APIRouter
from fastapi.responses import JSONResponse

from app.models.request.create_pet_request import PetRequest
from app.openai.prompt import get_pet_system_prompt
from app.openai.llm import get_response_from_llm

llm_api = APIRouter(
    prefix="/pets",
    tags=["pets"]
)

# 반려견 생성
@llm_api.post("/")
async def create_pet(pet: PetRequest):
    

    return JSONResponse(status_code=201)