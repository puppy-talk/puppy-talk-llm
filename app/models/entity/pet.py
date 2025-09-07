from app.models.enum.gender import Gender
from sqlalchemy import Column, String, Integer, Text, JSON
from sqlalchemy.dialects.mysql import ENUM as MySQLEnum

from .base import BaseModel

class Pet(BaseModel):
    __abstract__ = False
    __tablename__ = "pet"

    owner_id = Column(Integer, nullable=False)
    name = Column(String(255), nullable=False)
    age = Column(Integer, nullable=False)
    gender = Column(
        MySQLEnum(*[g.value for g in Gender]),
        nullable=False,
        default=Gender.UNKNOWN.value
    )
    personalities = Column(JSON, nullable=False)
    tone = Column(Text, nullable=False)