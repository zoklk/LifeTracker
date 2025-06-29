import streamlit as st
from datetime import datetime, date

def show_user_info():
    """사용자 정보 설정"""
    st.header("👤 사용자 정보")
    st.subheader("기본 프로필 관리")
    
    st.info("🚧 이 기능은 추후 구현될 예정입니다.")
    
    # 예정된 UI 미리보기
    col1, col2 = st.columns(2)
    with col1:
        st.text_input("이름", value="사용자", disabled=True)
        st.number_input("키 (cm)", value=170.0, disabled=True)
        st.selectbox("성별", ["남성", "여성"], disabled=True)
    with col2:
        st.number_input("나이", value=25, disabled=True)
        st.number_input("현재 체중 (kg)", value=70.0, disabled=True)
        st.date_input("가입일", value=date.today(), disabled=True)
    
    st.button("프로필 업데이트", disabled=True)

def show_goal_settings():
    """목표 설정"""
    st.header("🎯 목표 설정")
    st.subheader("개인 목표 관리")
    
    st.info("🚧 이 기능은 추후 구현될 예정입니다.")
    
    # 체중 목표
    st.subheader("⚖️ 체중 목표")
    col1, col2 = st.columns(2)
    with col1:
        st.number_input("목표 체중 (kg)", disabled=True)
    with col2:
        st.date_input("목표 달성일", disabled=True)
    
    # 영양 목표  
    st.subheader("🍽️ 영양 목표")
    col1, col2 = st.columns(2)
    with col1:
        st.number_input("일일 목표 칼로리", disabled=True)
    with col2:
        st.number_input("일일 목표 단백질 (g)", disabled=True)
    
    # 운동 목표
    st.subheader("🏃‍♂️ 운동 목표")
    st.number_input("주간 목표 운동시간 (시간)", disabled=True)
    
    st.button("목표 설정 저장", disabled=True)

def show_data_management():
    """데이터 관리"""
    st.header("📊 데이터 관리")
    st.subheader("데이터 백업/복원")
    
    st.info("🚧 이 기능은 추후 구현될 예정입니다.")
    
    # 통계 정보
    st.subheader("📈 데이터 통계")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("총 기록 일수", "-- 일")
    with col2:
        st.metric("총 식사 기록", "-- 건")
    with col3:
        st.metric("총 프로젝트", "-- 개")
    
    # 데이터 관리 기능
    st.subheader("🔧 데이터 관리")
    col1, col2 = st.columns(2)
    with col1:
        st.button("📤 데이터 내보내기", disabled=True)
        st.info("CSV 형태로 모든 데이터를 내보냅니다")
    with col2:
        st.button("📥 데이터 가져오기", disabled=True)
        st.info("백업 파일에서 데이터를 복원합니다")
    
    st.divider()
    st.subheader("⚠️ 위험한 작업")
    st.button("🗑️ 모든 데이터 삭제", disabled=True, type="secondary")
    st.warning("이 작업은 되돌릴 수 없습니다!")

def show_system_settings():
    """시스템 설정"""
    st.header("🔧 시스템 설정")
    st.subheader("앱 환경 설정")
    
    st.info("🚧 이 기능은 추후 구현될 예정입니다.")
    
    # 알림 설정
    st.subheader("🔔 알림 설정")
    st.checkbox("체중 기록 알림", disabled=True)
    st.checkbox("식사 기록 알림", disabled=True)
    st.checkbox("운동 기록 알림", disabled=True)
    
    # 표시 설정
    st.subheader("🎨 표시 설정")
    st.selectbox("테마", ["라이트", "다크"], disabled=True)
    st.selectbox("차트 색상", ["기본", "컬러풀", "모노크롬"], disabled=True)
    
    # 데이터베이스 설정
    st.subheader("🗄️ 데이터베이스")
    st.info(f"데이터베이스 위치: /data/lifetracker.db")
    st.info(f"마지막 백업: 구현 예정")
    
    # 앱 정보
    st.subheader("ℹ️ 앱 정보")
    st.info("LifeTracker v2.1")
    st.info("Phase 4 개발 중")
    st.info(f"현재 시간: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    st.button("설정 저장", disabled=True)

def show_settings_page():
    """설정 페이지 - 탭 방식 (레거시)"""
    st.header("⚙️ 설정")
    st.subheader("사용자 설정 & 시스템 관리")
    
    # 준비 중 메시지
    st.info("🚧 이 기능은 추후 구현될 예정입니다.")
    
    # 미리보기용 탭 레이아웃
    tab1, tab2, tab3, tab4 = st.tabs(["👤 사용자 정보", "🎯 목표 설정", "📊 데이터 관리", "🔧 시스템 설정"])
    
    with tab1:
        show_user_info()
    
    with tab2:
        show_goal_settings()
    
    with tab3:
        show_data_management()
    
    with tab4:
        show_system_settings()
