"""
건강 관련 엔티티 모델들
"""

from sqlalchemy import Column, Integer, String, Float, DateTime, Date, Time, Text, Boolean, ForeignKey
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from models.database.base import Base

class WeightRecord(Base):
    __tablename__ = 'weight_records'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    date = Column(Date, nullable=False)
    weight = Column(Float, nullable=False)
    created_at = Column(DateTime, default=func.now())
    
    # 관계 설정
    user = relationship("User", backref="weight_records")
    
    def __repr__(self):
        return f"<WeightRecord(user_id={self.user_id}, date={self.date}, weight={self.weight})>"

class MealSession(Base):
    __tablename__ = 'meal_sessions'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    date = Column(Date, nullable=False)
    meal_time = Column(Time, nullable=False)
    total_calories = Column(Integer, default=0)
    total_protein = Column(Float, default=0.0)
    notes = Column(Text)
    created_at = Column(DateTime, default=func.now())
    
    # 관계 설정
    user = relationship("User", backref="meal_sessions")
    meal_items = relationship("MealItem", backref="meal_session", cascade="all, delete-orphan")
    
    def __repr__(self):
        return f"<MealSession(user_id={self.user_id}, date={self.date}, time={self.meal_time})>"

class MealItem(Base):
    __tablename__ = 'meal_items'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    meal_session_id = Column(Integer, ForeignKey('meal_sessions.id'), nullable=False)
    food_name = Column(String(200), nullable=False)
    quantity = Column(String(50))
    calories = Column(Integer)
    protein = Column(Float)
    created_at = Column(DateTime, default=func.now())
    
    def __repr__(self):
        return f"<MealItem(food_name='{self.food_name}', calories={self.calories})>"

class SleepRecord(Base):
    __tablename__ = 'sleep_records'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    date = Column(Date, nullable=False)
    sleep_hours = Column(Float, nullable=False)
    condition_rating = Column(Integer)  # 1-5 점수
    notes = Column(Text)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())
    
    # 관계 설정
    user = relationship("User", backref="sleep_records")
    
    def __repr__(self):
        return f"<SleepRecord(user_id={self.user_id}, date={self.date}, hours={self.sleep_hours})>"

class ExerciseSession(Base):
    __tablename__ = 'exercise_sessions'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    date = Column(Date, nullable=False)
    duration_hours = Column(Float, nullable=False)
    is_completed = Column(Boolean, default=True)
    notes = Column(Text)
    created_at = Column(DateTime, default=func.now())
    
    # 관계 설정
    user = relationship("User", backref="exercise_sessions")
    body_parts = relationship("ExerciseBodyPart", backref="exercise_session", cascade="all, delete-orphan")
    
    def __repr__(self):
        return f"<ExerciseSession(user_id={self.user_id}, date={self.date}, duration={self.duration_hours})>"

class BodyPart(Base):
    __tablename__ = 'body_parts'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False, unique=True)
    
    def __repr__(self):
        return f"<BodyPart(name='{self.name}')>"

class ExerciseBodyPart(Base):
    __tablename__ = 'exercise_body_parts'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    exercise_session_id = Column(Integer, ForeignKey('exercise_sessions.id'), nullable=False)
    body_part_id = Column(Integer, ForeignKey('body_parts.id'), nullable=False)
    
    # 관계 설정
    body_part = relationship("BodyPart")
    
    def __repr__(self):
        return f"<ExerciseBodyPart(exercise_id={self.exercise_session_id}, body_part_id={self.body_part_id})>"

class UserFoodDatabase(Base):
    __tablename__ = 'user_food_database'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    food_name = Column(String(200), nullable=False)
    default_unit = Column(String(10), nullable=False)  # '개' 또는 'g'
    calories_per_unit = Column(Float, nullable=False)
    protein_per_unit = Column(Float, nullable=False)
    usage_count = Column(Integer, default=1)
    last_used = Column(DateTime, default=func.now())
    
    # 관계 설정
    user = relationship("User", backref="food_database")
    
    def __repr__(self):
        return f"<UserFoodDatabase(user_id={self.user_id}, food='{self.food_name}')>"
