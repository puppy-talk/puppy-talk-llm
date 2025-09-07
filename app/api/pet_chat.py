from fastapi import APIRouter, Response

from app.crud.pet_chat import ChatCrud
from app.models.request.create_chat_message_request import CreateChatMessageRequest

pet_chat_api = APIRouter(tags=["pet-chat"])

# 채팅방 메시지 전송
# TODO: ws 연결
@pet_chat_api.post("/{room_id}")
def create_chat_message(room_id: int, chat_request: CreateChatMessageRequest):
    ChatCrud.create_chat_message(room_id=room_id, chat_request=chat_request)
    return Response(status_code=201)

# 채팅방 입장 시 기존 메시지 출력
