import json

from fastapi import APIRouter

from app.models.request.create_pet_request import PetRequest
from app.openai.prompt import get_pet_system_prompt
from app.openai.llm import get_response_from_llm

llm_api = APIRouter(tags=["pet-chat"])