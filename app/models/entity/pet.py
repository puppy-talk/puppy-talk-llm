from sqlalchemy import Column, String, Integer, Text, JSON
from .base import BaseModel

class Pet(BaseModel):
    __abstract__ = False
    __tablename__ = "pet"

    owner_id = Column(Integer, nullable=False)
    name = Column(String(255), nullable=False)
    age = Column(Integer, nullable=False)
    sex = Column(String(10), nullable=False)
    personalities = Column(JSON, nullable=False)
    tone = Column(Text, nullable=False)