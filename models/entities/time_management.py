"""
시간 관리 관련 엔티티 모델들
"""

from sqlalchemy import Column, Integer, String, Float, DateTime, Date, Text, ForeignKey
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from models.database.base import Base

class Project(Base):
    __tablename__ = 'projects'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    name = Column(String(200), nullable=False)
    category = Column(String(50), nullable=False)  # work, personal, study, health, other
    start_date = Column(Date, nullable=False)
    end_date = Column(Date, nullable=False)
    target_value = Column(Integer, nullable=False)
    current_value = Column(Integer, default=0)
    unit_type = Column(String(50), nullable=False)  # pages, videos, chapters, hours, exercises, other
    status = Column(String(20), default='active')  # active, completed, paused, cancelled
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())
    
    # 관계 설정
    user = relationship("User", backref="projects")
    project_logs = relationship("ProjectLog", backref="project", cascade="all, delete-orphan")
    
    @property
    def progress_percent(self):
        """진행률 계산 (0-100)"""
        if self.target_value == 0:
            return 0
        return round((self.current_value * 100.0) / self.target_value, 1)
    
    def __repr__(self):
        return f"<Project(name='{self.name}', progress={self.progress_percent}%)>"

class ProjectLog(Base):
    __tablename__ = 'project_logs'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    project_id = Column(Integer, ForeignKey('projects.id'), nullable=False)
    date = Column(Date, nullable=False)
    work_description = Column(Text, nullable=False)
    hours_spent = Column(Float, nullable=False)
    progress_added = Column(Integer, nullable=False)
    created_at = Column(DateTime, default=func.now())
    
    def __repr__(self):
        return f"<ProjectLog(project_id={self.project_id}, date={self.date}, hours={self.hours_spent})>"

class OtherTimeCategory(Base):
    __tablename__ = 'other_time_categories'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False, unique=True)
    type = Column(String(20), nullable=False)  # waste, essential, other
    color = Column(String(7), default='#FF6B6B')  # 헥스 컬러
    created_at = Column(DateTime, default=func.now())
    
    # 관계 설정
    time_logs = relationship("OtherTimeLog", backref="category")
    
    def __repr__(self):
        return f"<OtherTimeCategory(name='{self.name}', type='{self.type}')>"

class OtherTimeLog(Base):
    __tablename__ = 'other_time_logs'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    category_id = Column(Integer, ForeignKey('other_time_categories.id'), nullable=False)
    date = Column(Date, nullable=False)
    hours_spent = Column(Float, nullable=False)
    description = Column(Text)
    created_at = Column(DateTime, default=func.now())
    
    # 관계 설정
    user = relationship("User", backref="other_time_logs")
    
    def __repr__(self):
        return f"<OtherTimeLog(user_id={self.user_id}, date={self.date}, hours={self.hours_spent})>"
