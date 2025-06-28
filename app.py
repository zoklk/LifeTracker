import streamlit as st
import pandas as pd
from datetime import datetime

#1: 초기 페이지 설정
st.set_page_config(
    page_title="LifeTracker",
    page_icon="🏃‍♂️",
    layout="wide"
)

#2: 메인 타이틀
st.title("🏃‍♂️ LifeTracker")
st.subheader("건강 데이터 추적 & 프로젝트 관리")

#3: 현재 시간 표시
st.write(f"현재 시간: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

#4: 기본 테스트 섹션
st.header("🎉 Docker 환경 테스트")

col1, col2 = st.columns(2)

with col1:
    st.success("✅ Streamlit 정상 작동")
    st.info("✅ Docker 컨테이너 실행")

with col2:
    st.warning("⚠️ 데이터베이스 연결 대기")
    st.error("❌ 주요 기능 구현 대기")

#5: 간단한 테스트 데이터
test_data = pd.DataFrame({
    'Date': ['2024-01-01', '2024-01-02', '2024-01-03'],
    'Weight': [70.5, 70.3, 70.1],
    'Calories': [2000, 1950, 2100]
})

st.header("📊 테스트 데이터")
st.dataframe(test_data)

#6: phase 3 이후
st.header("🚀 다음 단계")
st.markdown("""
**Phase 2 완료 후 진행사항:**
- ✅ Docker 환경 구축
- ⏳ 데이터베이스 연결
- ⏳ 건강 트래킹 기능
- ⏳ 분석 및 예측 기능
""")