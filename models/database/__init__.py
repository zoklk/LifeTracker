"""
SQLAlchemy 기반 데이터베이스 모듈
ORM을 통한 데이터베이스 접근을 제공합니다.
"""

from .connection import db_manager, init_database, check_connection
from .base import get_session, create_tables, drop_tables
from ..entities import *  # 모든 엔티티 import

# 주요 함수들을 모듈 레벨에서 직접 사용할 수 있도록 export
__all__ = [
    'db_manager',
    'init_database', 
    'check_connection',
    'get_session',
    'create_tables',
    'drop_tables',
    # 엔티티들
    'User',
    'WeightRecord', 'MealSession', 'MealItem', 'SleepRecord',
    'ExerciseSession', 'BodyPart', 'ExerciseBodyPart', 'UserFoodDatabase',
    'Project', 'ProjectLog', 'OtherTimeCategory', 'OtherTimeLog'
]
