"""
SQLAlchemy 기반 데이터베이스 연결 관리
기존 Raw SQL 방식을 대체합니다.
"""

from sqlalchemy.orm import Session
from contextlib import contextmanager
from models.database.base import engine, SessionLocal, get_session, create_tables
import logging

logger = logging.getLogger(__name__)

class DatabaseManager:
    """SQLAlchemy 기반 데이터베이스 매니저"""
    
    def __init__(self):
        self.engine = engine
        self.SessionLocal = SessionLocal
    
    @contextmanager
    def get_session_context(self):
        """컨텍스트 매니저를 통한 안전한 세션 관리"""
        session = get_session()
        try:
            yield session
            session.commit()
        except Exception as e:
            session.rollback()
            logger.error(f"데이터베이스 작업 실패: {e}")
            raise
        finally:
            session.close()
    
    def check_connection(self) -> bool:
        """데이터베이스 연결 상태 확인"""
        try:
            with self.get_session_context() as session:
                session.execute("SELECT 1").fetchone()
                logger.info("✅ SQLAlchemy 데이터베이스 연결 성공")
                return True
        except Exception as e:
            logger.error(f"❌ SQLAlchemy 데이터베이스 연결 실패: {e}")
            return False
    
    def init_database(self):
        """데이터베이스 초기화 (테이블 생성 + 기본 데이터)"""
        try:
            # 테이블 생성
            create_tables()
            
            # 기본 데이터 삽입
            self._insert_default_data()
            
            logger.info("✅ SQLAlchemy 데이터베이스 초기화 완료")
            return True
        except Exception as e:
            logger.error(f"❌ SQLAlchemy 데이터베이스 초기화 실패: {e}")
            return False
    
    def _insert_default_data(self):
        """기본 데이터 삽입"""
        # 엔티티들을 함수 내부에서 import (순환 import 방지)
        from models.entities.health import BodyPart
        from models.entities.time_management import OtherTimeCategory
        
        with self.get_session_context() as session:
            # 운동 부위 기본 데이터
            body_parts_data = [
                '하체', '가슴', '등', '이두', '삼두',
                '어깨(전면)', '어깨(측면)', '어깨(후면)', '복근'
            ]
            
            for part_name in body_parts_data:
                existing = session.query(BodyPart).filter(BodyPart.name == part_name).first()
                if not existing:
                    body_part = BodyPart(name=part_name)
                    session.add(body_part)
            
            # 기타시간 카테고리 기본 데이터
            time_categories_data = [
                # 낭비시간
                ('SNS', 'waste', '#FF6B6B'),
                ('게임', 'waste', '#4ECDC4'),
                ('유튜브', 'waste', '#45B7D1'),
                ('쇼핑', 'waste', '#96CEB4'),
                # 필수시간
                ('학교수업', 'essential', '#A8E6CF'),
                ('출근', 'essential', '#88D8C0'),
                ('통근', 'essential', '#78C2AD'),
                ('식사준비', 'essential', '#68B69A'),
                # 기타
                ('개인관리', 'other', '#FFEAA7'),
                ('휴식', 'other', '#FFCC5C')
            ]
            
            for name, type_val, color in time_categories_data:
                existing = session.query(OtherTimeCategory).filter(OtherTimeCategory.name == name).first()
                if not existing:
                    category = OtherTimeCategory(name=name, type=type_val, color=color)
                    session.add(category)

# 싱글톤 인스턴스
db_manager = DatabaseManager()

# 호환성을 위한 래퍼 함수들
def init_database():
    """기존 함수명 호환성 유지"""
    return db_manager.init_database()

def check_connection():
    """기존 함수명 호환성 유지"""
    return db_manager.check_connection()
