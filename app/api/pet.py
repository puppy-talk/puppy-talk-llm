import json

from fastapi import APIRouter, Response

from app.models.request.create_pet_request import CreatePetRequest

pet_api = APIRouter(tags=["pets"])

# 반려견 생성
@pet_api.post("/")
async def create_pet(pet: CreatePetRequest):
    create_pet(pet)
    return Response(status_code=201)