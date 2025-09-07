from app.db.db import connect_database
from app.models.entity.pet import Pet
from app.models.request.create_chat_message_request import CreateChatMessageRequest
from app.models.request.create_pet_request import CreatePetRequest
from app.models.entity.message import Message

class ChatCrud:
    def create_chat_message(room_id: int, chat_request: CreateChatMessageRequest):
        message = Message(
            writer_id=1,
            room_id=1,
            message=chat_request.message
        )

        with connect_database() as db:
            db.add(message)
            db.commit()
            db.refresh(message)

        return message.id