import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime

def show_health_overview():
    """건강 종합 분석"""
    st.header("📊 건강 종합 분석")
    st.subheader("주간/월간 건강 데이터 종합")
    
    st.info("🚧 이 기능은 추후 구현될 예정입니다.")
    
    # 예정된 메트릭들
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("주간 평균 칼로리", "-- kcal", "-- kcal")
    with col2:
        st.metric("주간 평균 단백질", "-- g", "-- g")
    with col3:
        st.metric("평균 수면시간", "-- 시간", "-- 시간")
    with col4:
        st.metric("평균 컨디션", "-- / 5", "-- 점")
        
    st.markdown("#### 🎯 다음주 권장량")
    st.info("체중 변화 추세를 기반한 개인화된 권장 칼로리/단백질이 표시됩니다")

def show_weight_trend():
    """체중 변화 추이"""
    st.header("⚖️ 체중 변화 추이")
    st.subheader("체중 그래프 & 목표 달성 예측")
    
    st.info("🚧 이 기능은 추후 구현될 예정입니다.")
    
    # 샘플 차트 미리보기
    sample_data = pd.DataFrame({
        'date': pd.date_range('2024-01-01', periods=30, freq='D'),
        'weight': [70 + i*0.1 + (i%7)*0.3 for i in range(30)]
    })
    
    fig = px.line(sample_data, x='date', y='weight', 
                 title='체중 변화 추이 (샘플)')
    st.plotly_chart(fig, use_container_width=True)
    
    st.info("실제 데이터가 입력되면 정확한 분석이 제공됩니다")

def show_nutrition_analysis():
    """영양 섭취 분석"""
    st.header("🍽️ 영양 섭취 분석")
    st.subheader("칼로리/단백질 섭취 패턴")
    
    st.info("🚧 이 기능은 추후 구현될 예정입니다.")
    
    # 샘플 차트
    sample_nutrition = pd.DataFrame({
        'date': pd.date_range('2024-01-01', periods=7, freq='D'),
        'calories': [2000, 1950, 2100, 1800, 2200, 2050, 1900],
        'protein': [120, 115, 130, 110, 140, 125, 118]
    })
    
    fig2 = px.bar(sample_nutrition, x='date', y=['calories', 'protein'],
                 title='주간 영양 섭취 (샘플)')
    st.plotly_chart(fig2, use_container_width=True)

def show_sleep_pattern():
    """수면 패턴 분석"""
    st.header("💤 수면 패턴 분석")
    st.subheader("수면시간과 컨디션 상관관계")
    
    st.info("🚧 이 기능은 추후 구현될 예정입니다.")
    
    # 샘플 수면 데이터
    sample_sleep = pd.DataFrame({
        'date': pd.date_range('2024-01-01', periods=14, freq='D'),
        'sleep_hours': [7, 6.5, 8, 7.5, 6, 9, 8.5, 7, 6.5, 8, 7.5, 6, 7, 8],
        'condition': [4, 3, 5, 4, 2, 5, 5, 4, 3, 5, 4, 2, 4, 5]
    })
    
    fig3 = px.scatter(sample_sleep, x='sleep_hours', y='condition',
                     title='수면시간 vs 컨디션 상관관계 (샘플)')
    st.plotly_chart(fig3, use_container_width=True)
    
    st.markdown("#### 📋 수면 분석 결과")
    st.info("최적 수면시간 및 개선 권장사항이 표시됩니다")

def show_health_analysis_page():
    """건강 분석 페이지 - 탭 방식 (레거시)"""
    st.header("📈 건강 분석")
    st.subheader("건강 데이터 심화 분석 & 예측")
    
    # 준비 중 메시지
    st.info("🚧 이 기능은 추후 구현될 예정입니다.")
    
    # 미리보기용 탭 레이아웃
    tab1, tab2, tab3, tab4 = st.tabs(["📊 종합 분석", "⚖️ 체중 추이", "🍽️ 영양 분석", "💤 수면 패턴"])
    
    with tab1:
        show_health_overview()
    
    with tab2:
        show_weight_trend()
    
    with tab3:
        show_nutrition_analysis()
    
    with tab4:
        show_sleep_pattern()
