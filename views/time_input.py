import streamlit as st
from datetime import datetime, date

def show_project_time_input():
    """프로젝트 작업 시간 입력"""
    st.header("📊 프로젝트 작업")
    st.subheader(f"📅 {datetime.now().strftime('%Y년 %m월 %d일')}")
    
    st.info("🚧 이 기능은 추후 구현될 예정입니다.")
    
    # 예정된 UI 미리보기
    st.selectbox("프로젝트 선택", ["프로젝트 1", "프로젝트 2"], disabled=True)
    st.number_input("작업 시간 (시간)", disabled=True)
    st.text_area("작업 내용", disabled=True)
    st.number_input("진행도 (완료한 작업량)", disabled=True)
    st.button("시간 기록", disabled=True)

def show_other_time_input():
    """기타시간 기록"""
    st.header("🕐 기타시간")
    st.subheader(f"📅 {datetime.now().strftime('%Y년 %m월 %d일')}")
    
    st.info("🚧 이 기능은 추후 구현될 예정입니다.")
    
    # 예정된 UI 미리보기
    st.selectbox("카테고리", 
                ["낭비시간 (SNS, 게임, 유튜브)", "필수시간 (수업, 출근, 식사)", "기타 (휴식, 개인관리)"], 
                disabled=True)
    st.selectbox("세부 항목", ["선택해주세요"], disabled=True)
    st.number_input("소요 시간 (시간)", disabled=True)
    st.button("기타시간 기록", disabled=True)

def show_project_management():
    """프로젝트 관리"""
    st.header("📁 프로젝트 관리")
    st.subheader("프로젝트 생성 & 관리")
    
    st.info("🚧 이 기능은 추후 구현될 예정입니다.")
    
    # 예정된 UI 미리보기
    with st.expander("새 프로젝트 생성"):
        st.text_input("프로젝트명", disabled=True)
        st.selectbox("카테고리", ["업무", "개인", "학습", "건강", "기타"], disabled=True)
        st.date_input("시작일", disabled=True)
        st.date_input("목표 완료일", disabled=True)
        st.number_input("목표 수치 (페이지, 강의 수 등)", disabled=True)
        st.button("프로젝트 생성", disabled=True)
        
    st.markdown("#### 📋 현재 프로젝트 목록")
    st.info("등록된 프로젝트들이 여기에 표시됩니다")

def show_time_input_page():
    """시간 입력 페이지 - 탭 방식 (레거시)"""
    st.header("⏰ 시간 입력")
    st.subheader(f"📅 {datetime.now().strftime('%Y년 %m월 %d일')}")
    
    # 준비 중 메시지
    st.info("🚧 이 기능은 추후 구현될 예정입니다.")
    
    # 미리보기용 탭 레이아웃
    tab1, tab2, tab3 = st.tabs(["📊 프로젝트", "🕐 기타시간", "📁 프로젝트 관리"])
    
    with tab1:
        show_project_time_input()
    
    with tab2:
        show_other_time_input()
    
    with tab3:
        show_project_management()
