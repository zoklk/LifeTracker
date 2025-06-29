import streamlit as st
from datetime import datetime, date

def show_meal_input():
    """식사 기록 입력"""
    st.header("🍽️ 식사 기록")
    st.subheader(f"📅 {datetime.now().strftime('%Y년 %m월 %d일')}")
    
    st.info("🚧 이 기능은 추후 구현될 예정입니다.")
    
    # 예정된 UI 미리보기
    st.selectbox("식사 시간", ["아침", "점심", "저녁", "간식"], disabled=True)
    st.text_input("음식 검색", placeholder="예: 닭가슴살", disabled=True)
    col1, col2 = st.columns(2)
    with col1:
        st.number_input("칼로리 (kcal)", disabled=True)
    with col2:
        st.number_input("단백질 (g)", disabled=True)
    st.button("식사 기록 추가", disabled=True)

def show_weight_input():
    """체중 기록 입력"""
    st.header("⚖️ 체중 기록")
    st.subheader(f"📅 {datetime.now().strftime('%Y년 %m월 %d일')}")
    
    st.info("🚧 이 기능은 추후 구현될 예정입니다.")
    
    # 예정된 UI 미리보기
    st.number_input("현재 체중 (kg)", disabled=True)
    st.date_input("측정 날짜", value=date.today(), disabled=True)
    st.button("체중 기록", disabled=True)

def show_sleep_input():
    """수면 & 컨디션 입력"""
    st.header("💤 수면 & 컨디션")
    st.subheader(f"📅 {datetime.now().strftime('%Y년 %m월 %d일')}")
    
    st.info("🚧 이 기능은 추후 구현될 예정입니다.")
    
    # 예정된 UI 미리보기
    st.number_input("수면시간 (시간)", disabled=True)
    st.select_slider("오늘 컨디션", options=[1, 2, 3, 4, 5], disabled=True)
    st.button("수면 기록", disabled=True)

def show_exercise_input():
    """운동 기록 입력"""
    st.header("🏃‍♂️ 운동 기록")
    st.subheader(f"📅 {datetime.now().strftime('%Y년 %m월 %d일')}")
    
    st.info("🚧 이 기능은 추후 구현될 예정입니다.")
    
    # 예정된 UI 미리보기
    st.number_input("총 운동시간 (시간)", disabled=True)
    st.multiselect("운동 부위", 
                  ["하체", "가슴", "등", "이두", "삼두", "어깨", "복근"], 
                  disabled=True)
    st.text_area("운동 메모", disabled=True)
    st.button("운동 기록", disabled=True)

def show_health_input_page():
    """건강 입력 페이지 - 탭 방식 (레거시)"""
    st.header("🏥 건강 입력")
    st.subheader(f"📅 {datetime.now().strftime('%Y년 %m월 %d일')}")
    
    # 준비 중 메시지
    st.info("🚧 이 기능은 추후 구현될 예정입니다.")
    
    # 미리보기용 탭 레이아웃
    tab1, tab2, tab3, tab4 = st.tabs(["🍽️ 식사", "⚖️ 체중", "💤 수면", "🏃‍♂️ 운동"])
    
    with tab1:
        show_meal_input()
    
    with tab2:
        show_weight_input()
    
    with tab3:
        show_sleep_input()
    
    with tab4:
        show_exercise_input()
