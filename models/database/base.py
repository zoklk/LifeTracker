"""
SQLAlchemy Base 클래스 및 엔진 설정
"""

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

# Base 클래스 생성
Base = declarative_base()

# 데이터베이스 URL 설정
DB_PATH = "data/lifetracker.db"
DATABASE_URL = f"sqlite:///{DB_PATH}"

# 엔진 생성
engine = create_engine(
    DATABASE_URL,
    echo=False,  # SQL 로그 출력 (개발시 True로 변경)
    connect_args={"check_same_thread": False}  # SQLite 멀티스레드 지원
)

# 세션 팩토리 생성
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_session():
    """세션 인스턴스 반환"""
    return SessionLocal()

def create_tables():
    """모든 테이블 생성"""
    # data 디렉토리 생성
    os.makedirs("data", exist_ok=True)
    
    # 모든 테이블 생성
    Base.metadata.create_all(bind=engine)
    print("✅ 모든 테이블이 생성되었습니다.")

def drop_tables():
    """모든 테이블 삭제 (개발용)"""
    Base.metadata.drop_all(bind=engine)
    print("❌ 모든 테이블이 삭제되었습니다.")
