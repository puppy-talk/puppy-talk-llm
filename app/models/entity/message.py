from sqlalchemy import Column, String, Integer, Text, JSON
from sqlalchemy.dialects.mysql import ENUM as MySQLEnum

from .base import BaseModel

class Message(BaseModel):
    __abstract__ = False
    __tablename__ = "message"

    # TODO: 강아지 id, user id 구분 필요
    writer_id = Column(Integer, nullable=False)
    room_id = Column(Integer, nullable=False)
    message = Column(String(255), nullable=False)