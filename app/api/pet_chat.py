import json

from fastapi import APIRouter

from app.models.request.create_pet_request import PetRequest
from app.openai.prompt import get_pet_chat_prompt
from app.openai.llm import get_response_from_llm

llm_api = APIRouter(
    prefix="/pet-chat",
    tags=["pet-chat"]
)

@llm_api.post("/")
async def create_pet(pet: PetRequest):
    pet_prompt = get_pet_chat_prompt(pet)
    # 비동기 요청을 위한 AsyncOpenAI 사용
    llm_response = await get_response_from_llm(system_prompt="당신은 지금부터 강아지입니다.", user_prompt=pet_prompt)

    return { "content": llm_response.choices[0].message.content }