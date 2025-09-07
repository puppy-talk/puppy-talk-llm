from pydantic import BaseModel

class CreateChatMessageRequest(BaseModel):
    message: str