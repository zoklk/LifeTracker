import streamlit as st
from datetime import datetime

# Views 모듈 import - 개별 함수들
from views.today import show_today_page

# 건강 입력 개별 함수들
from views.health_input import (
    show_meal_input, 
    show_weight_input, 
    show_sleep_input, 
    show_exercise_input
)

# 시간 입력 개별 함수들  
from views.time_input import (
    show_project_time_input,
    show_other_time_input,
    show_project_management
)

# 건강 분석 개별 함수들
from views.health_analysis import (
    show_health_overview,
    show_weight_trend,
    show_nutrition_analysis,
    show_sleep_pattern
)

# 시간 분석 개별 함수들
from views.time_analysis import (
    show_project_progress,
    show_time_distribution,
    show_efficiency_analysis
)

# 설정 개별 함수들
from views.settings import (
    show_user_info,
    show_goal_settings,
    show_data_management,
    show_system_settings
)

# 데이터베이스 모듈 import
try:
    from models.database import init_database, check_connection
    DATABASE_AVAILABLE = True
except ImportError as e:
    DATABASE_AVAILABLE = False
    DB_ERROR = str(e)

# 페이지 설정
st.set_page_config(
    page_title="LifeTracker",
    page_icon="🏃‍♂️",
    layout="wide",
    initial_sidebar_state="expanded"
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

# 사이드바 네비게이션
st.sidebar.title("🏃‍♂️ LifeTracker")
st.sidebar.markdown("---")

# 세션 상태 초기화
if 'current_page' not in st.session_state:
    st.session_state.current_page = 'today'

# 네비게이션 메뉴 구조
menu_structure = {
    "📊 오늘 기록": {
        "key": "today",
        "function": show_today_page,
        "submenu": None
    },
    "🏥 건강 입력": {
        "key": "health_input", 
        "function": None,
        "submenu": {
            "🍽️ 식사 기록": {"key": "meal_input", "function": show_meal_input},
            "⚖️ 체중 기록": {"key": "weight_input", "function": show_weight_input},
            "💤 수면 기록": {"key": "sleep_input", "function": show_sleep_input},
            "🏃‍♂️ 운동 기록": {"key": "exercise_input", "function": show_exercise_input}
        }
    },
    "⏰ 시간 입력": {
        "key": "time_input",
        "function": None,
        "submenu": {
            "📊 프로젝트 작업": {"key": "project_time_input", "function": show_project_time_input},
            "🕐 기타시간": {"key": "other_time_input", "function": show_other_time_input},
            "📁 프로젝트 관리": {"key": "project_management", "function": show_project_management}
        }
    },
    "📈 건강 분석": {
        "key": "health_analysis",
        "function": None,
        "submenu": {
            "📊 종합 분석": {"key": "health_overview", "function": show_health_overview},
            "⚖️ 체중 추이": {"key": "weight_trend", "function": show_weight_trend},
            "🍽️ 영양 분석": {"key": "nutrition_analysis", "function": show_nutrition_analysis},
            "💤 수면 패턴": {"key": "sleep_pattern", "function": show_sleep_pattern}
        }
    },
    "📊 시간 분석": {
        "key": "time_analysis",
        "function": None,
        "submenu": {
            "📈 프로젝트 진행": {"key": "project_progress", "function": show_project_progress},
            "⏰ 시간 배분": {"key": "time_distribution", "function": show_time_distribution},
            "📊 효율성 분석": {"key": "efficiency_analysis", "function": show_efficiency_analysis}
        }
    },
    "⚙️ 설정": {
        "key": "settings",
        "function": None,
        "submenu": {
            "👤 사용자 정보": {"key": "user_info", "function": show_user_info},
            "🎯 목표 설정": {"key": "goal_settings", "function": show_goal_settings},
            "📊 데이터 관리": {"key": "data_management", "function": show_data_management},
            "🔧 시스템 설정": {"key": "system_settings", "function": show_system_settings}
        }
    }
}

# 사이드바 메뉴 렌더링
def render_sidebar_navigation():
    """GitHub 스타일 토글 네비게이션 렌더링"""
    
    for main_menu, config in menu_structure.items():
        
        # 단독 페이지 (오늘 기록)
        if config["submenu"] is None:
            if st.sidebar.button(main_menu, key=f"btn_{config['key']}", use_container_width=True):
                st.session_state.current_page = config["key"]
        
        # 서브메뉴가 있는 페이지
        else:
            # 현재 페이지가 이 메뉴 그룹에 속하는지 확인
            current_in_group = any(
                st.session_state.current_page == sub_config["key"] 
                for sub_config in config["submenu"].values()
            )
            
            # Expander로 토글 메뉴 구현
            with st.sidebar.expander(main_menu, expanded=current_in_group):
                for sub_menu, sub_config in config["submenu"].items():
                    # 현재 선택된 서브메뉴 하이라이트
                    is_current = st.session_state.current_page == sub_config["key"]
                    
                    # 버튼 스타일 (현재 페이지면 다른 색상)
                    button_type = "primary" if is_current else "secondary"
                    
                    if st.button(
                        sub_menu, 
                        key=f"btn_{sub_config['key']}", 
                        use_container_width=True,
                        type=button_type
                    ):
                        st.session_state.current_page = sub_config["key"]

# 네비게이션 렌더링
render_sidebar_navigation()

# 사이드바 상태 정보
st.sidebar.markdown("---")
st.sidebar.markdown("### 📊 상태 정보")

# 데이터베이스 상태
if DATABASE_AVAILABLE:
    if st.session_state.get('db_status') == 'success':
        st.sidebar.success("🟢 DB 연결됨")
    elif st.session_state.get('db_status') == 'failed':
        st.sidebar.error("🔴 DB 연결 실패")
    elif st.session_state.get('db_status') == 'error':
        st.sidebar.error("🔴 DB 오류")
    else:
        st.sidebar.warning("🟡 DB 초기화 중")
else:
    st.sidebar.error("🔴 DB 모듈 없음")

# 현재 시간
st.sidebar.info(f"🕐 {datetime.now().strftime('%H:%M:%S')}")

# 개발 상태
st.sidebar.markdown("---")
st.sidebar.markdown("### 🚀 개발 상태")
st.sidebar.info("📋 Phase 4 진행 중")
st.sidebar.info("🔧 GitHub 스타일 네비게이션")

# 메인 컨텐츠 영역
def main():
    """메인 컨텐츠 렌더링"""
    
    current_page = st.session_state.current_page
    
    # 현재 페이지에 해당하는 함수 찾기 및 실행
    page_function = None
    
    # 모든 메뉴에서 현재 페이지 키와 매칭되는 함수 찾기
    for main_menu, config in menu_structure.items():
        # 단독 페이지
        if config["submenu"] is None and config["key"] == current_page:
            page_function = config["function"]
            break
        # 서브메뉴 페이지
        elif config["submenu"] is not None:
            for sub_menu, sub_config in config["submenu"].items():
                if sub_config["key"] == current_page:
                    page_function = sub_config["function"]
                    break
            if page_function:
                break
    
    # 해당 페이지 함수 실행
    if page_function:
        page_function()
    else:
        st.error(f"페이지를 찾을 수 없습니다: {current_page}")

# 메인 앱 실행
if __name__ == "__main__":
    main()
