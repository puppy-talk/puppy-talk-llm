import json
import asyncio

from fastapi import APIRouter, HTTPException

from app.models.request.create_pet_request import PetRequest
from app.openai.prompt import get_pet_system_prompt
from app.openai.llm import get_response_from_llm
from app.openai.mcp_client import MySQLMCPClient, get_pet_info, get_owner_pets

llm_api = APIRouter(tags=["pet-chat"])

@llm_api.get("/pet/{pet_id}")
async def get_pet_by_id(pet_id: int):
    """MCP를 통해 펫 정보 조회"""
    try:
        pet_info = await get_pet_info(pet_id)
        if not pet_info:
            raise HTTPException(status_code=404, detail="Pet not found")
        return {"pet": pet_info}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error fetching pet: {str(e)}")

@llm_api.get("/owner/{owner_id}/pets")
async def get_pets_by_owner_id(owner_id: int):
    """MCP를 통해 소유자의 펫 목록 조회"""
    try:
        pets = await get_owner_pets(owner_id)
        return {"pets": pets}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error fetching pets: {str(e)}")

@llm_api.post("/chat/{pet_id}")
async def chat_with_pet(pet_id: int, message: dict):
    """MCP로 펫 정보를 조회하고 채팅 응답 생성"""
    try:
        # MCP를 통해 펫 정보 조회
        pet_info = await get_pet_info(pet_id)
        if not pet_info:
            raise HTTPException(status_code=404, detail="Pet not found")
        
        # 펫 정보를 바탕으로 시스템 프롬프트 생성
        pet_request = PetRequest(
            name=pet_info['name'],
            age=int(pet_info['age']),
            gender=pet_info['gender'],
            personalities=json.loads(pet_info['personalities']) if isinstance(pet_info['personalities'], str) else pet_info['personalities'],
            tone=pet_info['tone']
        )
        
        system_prompt = get_pet_system_prompt(pet_request)
        
        # LLM 응답 생성
        response = get_response_from_llm(
            system_prompt=system_prompt,
            user_message=message.get("content", "")
        )
        
        return {"response": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error in chat: {str(e)}")

# 채팅방 메시지 전송

# 채팅방 입장 시 기존 메시지 출력