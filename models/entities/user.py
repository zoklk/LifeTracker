"""
User 엔티티 모델
"""

from sqlalchemy import Column, Integer, String, Float, DateTime, Date
from sqlalchemy.sql import func
from models.database.base import Base

class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    height = Column(Float, nullable=False)  # cm
    current_weight = Column(Float)  # kg
    target_weight = Column(Float)   # kg
    target_date = Column(Date)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())
    
    def __repr__(self):
        return f"<User(id={self.id}, name='{self.name}', height={self.height})>"
    
    def to_dict(self):
        """딕셔너리로 변환"""
        return {
            'id': self.id,
            'name': self.name,
            'height': self.height,
            'current_weight': self.current_weight,
            'target_weight': self.target_weight,
            'target_date': self.target_date,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }
