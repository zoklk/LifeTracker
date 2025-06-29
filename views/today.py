import streamlit as st
from datetime import datetime

def show_today_page():
    """오늘 기록 페이지 - 일일 요약 + 통합 대시보드"""
    
    st.header("📊 오늘 기록")
    st.subheader(f"📅 {datetime.now().strftime('%Y년 %m월 %d일 (%A)')}")
    
    # 준비 중 메시지
    st.info("🚧 이 기능은 추후 구현될 예정입니다.")
    
    # 미리보기용 레이아웃
    st.markdown("---")
    st.markdown("### 📋 예정된 기능")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric(
            label="📊 오늘 칼로리",
            value="-- kcal",
            delta="목표 대비"
        )
        
    with col2:
        st.metric(
            label="⚖️ 현재 체중",
            value="-- kg",
            delta="어제 대비"
        )
        
    with col3:
        st.metric(
            label="⏰ 총 작업시간",
            value="-- 시간",
            delta="계획 대비"
        )
    
    st.markdown("---")
    
    # 예정된 섹션들
    st.markdown("#### 🍽️ 오늘의 식사")
    st.info("식사 기록이 여기에 표시됩니다")
    
    st.markdown("#### 🏃‍♂️ 오늘의 운동")
    st.info("운동 기록이 여기에 표시됩니다")
    
    st.markdown("#### 📈 프로젝트 진행")
    st.info("프로젝트 진행상황이 여기에 표시됩니다")
    
    st.markdown("#### 💤 수면 & 컨디션")
    st.info("수면시간과 컨디션 평가가 여기에 표시됩니다")
