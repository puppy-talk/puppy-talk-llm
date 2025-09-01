from sqlalchemy import Column, Integer, DateTime, Boolean
from datetime import datetime

from app.db.db import Base

class BaseModel(Base):
    __abstract__ = True   # 해당 클래스가 테이블로 생성되지 않도록 설정
    
    id = Column(Integer, primary_key = True, autoincrement = True)
    is_deleted = Column(Boolean, default = False)
    created_at = Column(DateTime, default = datetime.now)
    # onupdate 옵션: 해당 레코드가 업데이트될 때마다 자동으로 현재 시각으로 필드값 갱신
    updated_at = Column(DateTime, default = datetime.now, onupdate = datetime.now)