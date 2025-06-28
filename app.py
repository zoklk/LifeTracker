import streamlit as st
import pandas as pd
from datetime import datetime

# 데이터베이스 모듈 import
try:
    from models.database import init_database, check_connection
    DATABASE_AVAILABLE = True
except ImportError as e:
    DATABASE_AVAILABLE = False
    DB_ERROR = str(e)

#1: 초기 페이지 설정
st.set_page_config(
    page_title="LifeTracker",
    page_icon="🏃‍♂️",
    layout="wide"
)

# 데이터베이스 초기화 (앱 시작 시 한 번만)
if DATABASE_AVAILABLE and 'database_initialized' not in st.session_state:
    with st.spinner('데이터베이스 초기화 중...'):
        try:
            if init_database():
                st.session_state.database_initialized = True
                st.session_state.db_status = 'success'
            else:
                st.session_state.db_status = 'failed'
        except Exception as e:
            st.session_state.db_status = 'error'
            st.session_state.db_error = str(e)

#2: 메인 타이틀
st.title("🏃‍♂️ LifeTracker")
st.subheader("건강 데이터 추적 & 프로젝트 관리")

#3: 데이터베이스 상태 표시
if DATABASE_AVAILABLE:
    if st.session_state.get('db_status') == 'success':
        st.success("✅ 데이터베이스 연결 성공!")
    elif st.session_state.get('db_status') == 'failed':
        st.error("❌ 데이터베이스 초기화 실패")
    elif st.session_state.get('db_status') == 'error':
        st.error(f"❌ 데이터베이스 오류: {st.session_state.get('db_error', 'Unknown error')}")
    else:
        st.info("⏳ 데이터베이스 초기화 대기 중...")
else:
    st.error(f"❌ 데이터베이스 모듈 로드 실패: {DB_ERROR}")

#4: 현재 시간 표시
st.write(f"현재 시간: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

#5: 기본 테스트 섹션
st.header("🎉 Docker 환경 테스트")

col1, col2 = st.columns(2)

with col1:
    st.success("✅ Streamlit 정상 작동")
    st.info("✅ Docker 컨테이너 실행")

with col2:
    if DATABASE_AVAILABLE and st.session_state.get('db_status') == 'success':
        st.success("✅ 데이터베이스 연결 성공")
        st.success("✅ 주요 기능 준비 완료")
    else:
        st.warning("⚠️ 데이터베이스 연결 대기")
        st.error("❌ 주요 기능 구현 대기")

#6: 간단한 테스트 데이터
test_data = pd.DataFrame({
    'Date': ['2024-01-01', '2024-01-02', '2024-01-03'],
    'Weight': [70.5, 70.3, 70.1],
    'Calories': [2000, 1950, 2100]
})

st.header("📊 테스트 데이터")
st.dataframe(test_data)

#7: Phase 3 완료 상태
st.header("🚀 다음 단계")

# 데이터베이스 상태에 따른 진행상황 표시
if DATABASE_AVAILABLE and st.session_state.get('db_status') == 'success':
    st.markdown("""
    **Phase 3 완료 상황:**
    - ✅ Docker 환경 구축
    - ✅ 데이터베이스 연결 및 초기화
    - ✅ 13개 테이블 생성 완료
    - ✅ 기본 데이터 삽입 완료
    - ⏳ 건강 트래킹 UI 구현 (다음 단계)
    - ⏳ 분석 및 예측 기능 (다음 단계)
    """)

    # 데이터베이스 연결 테스트 버튼
    if st.button("🔧 데이터베이스 상세 테스트 실행"):
        st.info("별도 터미널에서 다음 명령어를 실행하세요:")
        st.code("python test_database_docker.py")

else:
    st.markdown("""
    **Phase 2 완료 후 진행사항:**
    - ✅ Docker 환경 구축
    - ❌ 데이터베이스 연결 실패
    - ⏳ 건강 트래킹 기능
    - ⏳ 분석 및 예측 기능
    """)

    st.warning("데이터베이스 모듈을 먼저 설정해주세요!")
