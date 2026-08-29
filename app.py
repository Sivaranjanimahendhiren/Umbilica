"""
UMBILICA - AI-Powered Maternal, Fetal & Neonatal Healthcare Platform
A premium, production-quality healthcare application built with Streamlit
"""

import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import plotly.graph_objects as go
import plotly.express as px
from PIL import Image
import io
from config import *

# Page config
st.set_page_config(
    page_title="UMBILICA - Maternal & Neonatal Care",
    page_icon="🏥",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Custom CSS styling
st.markdown("""
<style>
    /* Main theme colors */
    :root {
        --primary-pink: #EC0A7A;
        --deep-pink: #C90062;
        --soft-pink: #FCE4EF;
        --blush: #FFF4F8;
        --white: #FFFFFF;
        --text-dark: #000000;
        --text-secondary: #333333;
    }
    
    /* Global styles - WHITE BACKGROUND ONLY */
    body, .main, [data-testid="stMain"], section {
        font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Roboto', sans-serif;
        background-color: #FFFFFF !important;
        color: #000000 !important;
    }
    
    /* Sidebar styling - WHITE with pink accents */
    [data-testid="stSidebar"] {
        background-color: #FFFFFF !important;
        border-right: 2px solid #EC0A7A;
    }
    
    /* Remove any dark backgrounds */
    .stApp, .stAppView, [data-testid="stAppViewContainer"] {
        background-color: #FFFFFF !important;
    }
    
    /* Text styling - PURE BLACK */
    p, h1, h2, h3, h4, h5, h6, span, div {
        color: #000000 !important;
    }
    
    /* Custom card styling - SOFT PINK BACKGROUND */
    .metric-card {
        background: linear-gradient(135deg, #FCE4EF 0%, #FFF4F8 100%);
        border-radius: 12px;
        padding: 20px;
        border: 2px solid #EC0A7A;
    }
    
    /* Health score card - HOT PINK */
    .health-score-card {
        background: linear-gradient(135deg, #EC0A7A 0%, #C90062 100%);
        color: #FFFFFF !important;
        border-radius: 16px;
        padding: 24px;
        box-shadow: 0 4px 15px rgba(236, 10, 122, 0.3);
    }
    
    .health-score-card p, .health-score-card h1, .health-score-card h2, .health-score-card h3, .health-score-card h4, .health-score-card span {
        color: #FFFFFF !important;
    }
    
    /* Baby card styling - PINK */
    .baby-card-pink {
        background: linear-gradient(135deg, #FFB3D9 0%, #FFE4F0 100%);
        border-radius: 12px;
        padding: 20px;
        border: 2px solid #EC0A7A;
    }
    
    .baby-card-pink p, .baby-card-pink h2, .baby-card-pink h3, .baby-card-pink h4 {
        color: #000000 !important;
    }
    
    .baby-card-blue {
        background: linear-gradient(135deg, #87CEEB 0%, #E0F6FF 100%);
        border-radius: 12px;
        padding: 20px;
        border: 2px solid #0288D1;
    }
    
    .baby-card-blue p, .baby-card-blue h2, .baby-card-blue h3, .baby-card-blue h4 {
        color: #000000 !important;
    }
    
    /* Button styling */
    .stButton > button {
        border-radius: 8px;
        border: 2px solid #EC0A7A;
        padding: 10px 20px;
        font-weight: 600;
        transition: all 0.3s ease;
        background-color: #EC0A7A !important;
        color: #FFFFFF !important;
    }
    
    .stButton > button:hover {
        background-color: #C90062 !important;
        border-color: #C90062 !important;
    }
    
    /* Input styling */
    .stTextInput, .stNumberInput, .stSelectbox {
        background-color: #FFFFFF !important;
    }
    
    input, select, textarea {
        background-color: #FFF4F8 !important;
        border: 2px solid #EC0A7A !important;
        color: #000000 !important;
    }
    
    /* Tab styling */
    .stTabs [data-baseweb="tab-list"] {
        background-color: #FFFFFF !important;
        border-bottom: 2px solid #EC0A7A;
    }
    
    .stTabs [aria-selected="true"] {
        border-bottom: 3px solid #EC0A7A !important;
        color: #EC0A7A !important;
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state
if 'authenticated' not in st.session_state:
    st.session_state.authenticated = False
if 'user_role' not in st.session_state:
    st.session_state.user_role = None
if 'baby_gender' not in st.session_state:
    st.session_state.baby_gender = "female"
if 'care_mode' not in st.session_state:
    st.session_state.care_mode = "maternal"  # maternal or neonatal

# Authentication
def login_page():
    """Display login page"""
    st.set_page_config(layout="centered")
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown("""
        <h1 style='color: #EC0A7A; font-size: 48px; margin-bottom: 20px;'>🏥 UMBILICA</h1>
        <p style='font-size: 18px; color: #000000; margin-bottom: 30px; font-weight: 500;'>Intelligent Care. From Motherhood to New Beginnings.</p>
        <p style='font-size: 14px; color: #000000; line-height: 1.6;'>AI-powered maternal, fetal and neonatal healthcare intelligence.</p>
        """, unsafe_allow_html=True)
        
        st.markdown("---")
        
        st.markdown("""
        ### Why UMBILICA?
        - 🤰 Maternal Health Monitoring
        - 👶 Fetal Intelligence & Prediction
        - 🏥 Medical Image Analysis
        - 🤖 AI-Powered Risk Assessment
        - 💉 Vaccination Tracking
        - 📊 Real-time Health Dashboard
        """)
    
    with col2:
        st.markdown("<h2 style='color: #EC0A7A;'>Welcome Back, Mama</h2>", unsafe_allow_html=True)
        
        email = st.text_input("Email", value="demo@umbilica.ai")
        password = st.text_input("Password", type="password", value="Umbilica@123")
        
        col_a, col_b = st.columns(2)
        with col_a:
            remember = st.checkbox("Remember me")
        with col_b:
            st.write("")
            st.markdown("[Forgot password?](#)", help="Password reset feature")
        
        if st.button("Sign In", use_container_width=True, type="primary"):
            if email == "demo@umbilica.ai" and password == "Umbilica@123":
                st.session_state.authenticated = True
                st.session_state.user_role = "mother"
                st.success("Welcome back, Ananya!")
                st.rerun()
            else:
                st.error("Invalid credentials. Use demo@umbilica.ai / Umbilica@123")
        
        st.markdown("---")
        
        if st.button("🔑 Enter Demo Mode", use_container_width=True):
            st.session_state.authenticated = True
            st.session_state.user_role = "mother"
            st.session_state.care_mode = "maternal"
            st.success("Entering demo mode...")
            st.rerun()
        
        st.markdown("---")
        
        st.markdown("""
        <div style='text-align: center; margin-top: 30px; color: #000000;'>
            <p>Don't have an account? <strong>Sign up</strong> to start your Umbilica journey</p>
            <p style='font-size: 12px; margin-top: 20px;'>Demo Credentials:<br/>Email: demo@umbilica.ai<br/>Password: Umbilica@123</p>
        </div>
        """, unsafe_allow_html=True)

def logout():
    """Logout user"""
    st.session_state.authenticated = False
    st.session_state.user_role = None
    st.rerun()

# Main application
def main_app():
    """Main application interface"""
    
    # Sidebar navigation
    with st.sidebar:
        st.markdown("""
        <div style='text-align: center; padding: 20px 0; border-bottom: 2px solid #EC0A7A;'>
            <h2 style='color: #EC0A7A; margin: 0;'>🏥 UMBILICA</h2>
            <p style='color: #000000; font-size: 12px; margin: 5px 0; font-weight: 500;'>Healthcare Intelligence</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("---")
        
        # Navigation menu
        page = st.radio(
            "Navigation",
            [
                "🏠 Dashboard",
                "👩‍⚕️ Maternal Care",
                "🫀 Vitals",
                "👶 Fetal Intelligence",
                "🖼️ Medical Imaging",
                "🤖 AI Predictions",
                "📅 Appointments",
                "📝 Care Timeline",
                "👶 Neonatal Care",
                "💉 Vaccinations",
                "💊 Medications",
                "🏥 Follow-up Care",
                "📋 Reports",
                "🔔 Notifications",
                "💬 AI Assistant",
                "👤 Profile",
                "⚙️ Settings",
            ],
            label_visibility="collapsed"
        )
        
        st.markdown("---")
        
        # Emergency section
        st.markdown("""
        <div style='background-color: #FFE4E1; border-left: 4px solid #FF6B6B; padding: 12px; border-radius: 4px; margin-bottom: 20px;'>
            <strong style='color: #FF6B6B;'>🚨 Emergency</strong>
            <p style='margin: 10px 0 0 0; font-size: 12px; color: #000000;'>If experiencing severe symptoms, contact emergency services immediately.</p>
        </div>
        """, unsafe_allow_html=True)
        
        if st.button("📞 Call Emergency Services", use_container_width=True):
            st.warning("Emergency services: Dial 112 or your local emergency number")
        
        st.markdown("---")
        
        # User info
        st.markdown(f"""
        <div style='background-color: #FCE4EF; padding: 12px; border-radius: 8px; border: 2px solid #EC0A7A;'>
            <p style='margin: 0; font-size: 12px; color: #000000;'><strong>Logged in as</strong></p>
            <p style='margin: 5px 0; color: #EC0A7A; font-weight: bold;'>{DEMO_MOTHER['name']}</p>
        </div>
        """, unsafe_allow_html=True)
        
        if st.button("🚪 Logout", use_container_width=True):
            logout()
    
    # Route to pages based on selection
    if page == "🏠 Dashboard":
        dashboard_page()
    elif page == "👩‍⚕️ Maternal Care":
        maternal_care_page()
    elif page == "🫀 Vitals":
        vitals_page()
    elif page == "👶 Fetal Intelligence":
        fetal_intelligence_page()
    elif page == "🖼️ Medical Imaging":
        medical_imaging_page()
    elif page == "🤖 AI Predictions":
        ai_predictions_page()
    elif page == "📅 Appointments":
        appointments_page()
    elif page == "📝 Care Timeline":
        care_timeline_page()
    elif page == "👶 Neonatal Care":
        neonatal_page()
    elif page == "💉 Vaccinations":
        vaccinations_page()
    elif page == "💊 Medications":
        medications_page()
    elif page == "🏥 Follow-up Care":
        followup_page()
    elif page == "📋 Reports":
        reports_page()
    elif page == "🔔 Notifications":
        notifications_page()
    elif page == "💬 AI Assistant":
        ai_assistant_page()
    elif page == "👤 Profile":
        profile_page()
    elif page == "⚙️ Settings":
        settings_page()

# PAGE COMPONENTS START HERE

def dashboard_page():
    """Main maternal dashboard"""
    st.markdown(f"""
    <h1 style='color: #EC0A7A; margin-bottom: 10px;'>Good morning, {DEMO_MOTHER['name']} ❤️</h1>
    <p style='color: #71717A; font-size: 16px; margin-bottom: 20px;'>Week {DEMO_PREGNANCY['current_week']} • {DEMO_PREGNANCY['trimester']} Trimester</p>
    """, unsafe_allow_html=True)
    
    # Quick stats
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown("""
        <div class='metric-card'>
            <p style='margin: 0; color: #71717A; font-size: 12px;'>Maternal Health Score</p>
            <h2 style='margin: 10px 0 0 0; color: #EC0A7A;'>92<span style='font-size: 18px;'>/100</span></h2>
            <p style='margin: 5px 0 0 0; font-size: 12px; color: #4CAF50;'>📈 +3.2% • Stable</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        progress = (DEMO_PREGNANCY['current_week'] / 40) * 100
        st.markdown(f"""
        <div class='metric-card'>
            <p style='margin: 0; color: #71717A; font-size: 12px;'>Pregnancy Progress</p>
            <h2 style='margin: 10px 0 0 0; color: #EC0A7A;'>{DEMO_PREGNANCY['current_week']} weeks</h2>
            <p style='margin: 5px 0 0 0; font-size: 12px; color: #71717A;'>{progress:.0f}% completed</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class='metric-card'>
            <p style='margin: 0; color: #71717A; font-size: 12px;'>Fetal Heart Rate</p>
            <h2 style='margin: 10px 0 0 0; color: #EC0A7A;'>142 <span style='font-size: 14px;'>BPM</span></h2>
            <p style='margin: 5px 0 0 0; font-size: 12px; color: #4CAF50;'>✓ Normal • LIVE</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        st.markdown("""
        <div class='metric-card'>
            <p style='margin: 0; color: #71717A; font-size: 12px;'>AI Risk Score</p>
            <h2 style='margin: 10px 0 0 0; color: #4CAF50;'>8%</h2>
            <p style='margin: 5px 0 0 0; font-size: 12px; color: #4CAF50;'>✓ Low Risk</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Real-time monitoring section
    st.subheader("🔴 Live Maternal & Fetal Monitoring")
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Maternal heart rate chart
        vitals_df = generate_vitals_data(24)
        fig_hr = go.Figure()
        fig_hr.add_trace(go.Scatter(
            x=vitals_df['date'],
            y=vitals_df['heart_rate'],
            mode='lines+markers',
            name='Heart Rate',
            line=dict(color='#EC0A7A', width=3),
            fill='tozeroy',
            fillcolor='rgba(236, 10, 122, 0.1)',
        ))
        fig_hr.update_layout(
            title='Maternal Heart Rate (24h)',
            xaxis_title='Time',
            yaxis_title='BPM',
            hovermode='x unified',
            template='plotly_white',
            height=300,
        )
        st.plotly_chart(fig_hr, use_container_width=True)
    
    with col2:
        # Fetal heart rate chart
        fetal_df = generate_fetal_hr_data(24)
        fig_fetal = go.Figure()
        fig_fetal.add_trace(go.Scatter(
            x=fetal_df['time'],
            y=fetal_df['fetal_hr'],
            mode='lines+markers',
            name='Fetal HR',
            line=dict(color='#87CEEB', width=3),
            fill='tozeroy',
            fillcolor='rgba(135, 206, 235, 0.1)',
        ))
        fig_fetal.update_layout(
            title='Fetal Heart Rate (24h)',
            xaxis_title='Time',
            yaxis_title='BPM',
            hovermode='x unified',
            template='plotly_white',
            height=300,
        )
        st.plotly_chart(fig_fetal, use_container_width=True)
    
    st.markdown("---")
    
    # Next actions and upcoming appointments
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("📋 Next Care Actions")
        for action in DEMO_FOLLOW_UP_ACTIONS[:3]:
            priority_color = "#FF6B6B" if action['priority'] == "Urgent" else "#FFA500" if action['priority'] == "Important" else "#4CAF50"
            st.markdown(f"""
            <div style='background: #F5F5F5; padding: 12px; border-radius: 8px; margin-bottom: 8px; border-left: 4px solid {priority_color};'>
                <strong>{action['action']}</strong><br/>
                <small style='color: #71717A;'>Due: {action['due']} • <span style='color: {priority_color};'>{action['priority']}</span></small>
            </div>
            """, unsafe_allow_html=True)
    
    with col2:
        st.subheader("📅 Upcoming Appointments")
        upcoming = [a for a in DEMO_APPOINTMENTS if a['status'] == 'Upcoming']
        for appt in upcoming[:2]:
            st.markdown(f"""
            <div style='background: #F5F5F5; padding: 12px; border-radius: 8px; margin-bottom: 8px;'>
                <strong>Dr. {appt['doctor'].split()[-1]}</strong><br/>
                <small>{appt['type']}</small><br/>
                <small style='color: #71717A;'>📅 {appt['date']} at {appt['time']}</small>
            </div>
            """, unsafe_allow_html=True)

def maternal_care_page():
    """Maternal care overview"""
    st.markdown(f"<h1 style='color: #EC0A7A;'>Maternal Care</h1>", unsafe_allow_html=True)
    
    tab1, tab2, tab3 = st.tabs(["📊 Health Overview", "🔥 Current Vitals", "📈 Trends"])
    
    with tab1:
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.markdown("""
            <div class='health-score-card'>
                <p style='margin: 0; font-size: 14px; opacity: 0.9;'>Overall Health Score</p>
                <h1 style='margin: 10px 0 0 0;'>92/100</h1>
                <p style='margin: 10px 0 0 0; font-size: 12px; opacity: 0.9;'>Status: Stable • Trend: +3.2%</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.metric("Pregnancy Week", f"{DEMO_PREGNANCY['current_week']}/40", f"{DEMO_PREGNANCY['current_week']-27}w↑")
        
        with col3:
            st.metric("Expected Delivery", DEMO_PREGNANCY['edd'].strftime("%b %d, %Y"), "In 75 days")
        
        st.markdown("---")
        
        st.subheader("Key Health Indicators")
        indicators = pd.DataFrame({
            "Indicator": ["Blood Pressure", "Heart Rate", "Blood Glucose", "Hemoglobin", "BMI"],
            "Value": ["118/76 mmHg", "82 BPM", "96 mg/dL", "11.2 g/dL", "22.4"],
            "Status": ["✓ Normal", "✓ Normal", "✓ Normal", "✓ Normal", "✓ Healthy"],
            "Reference": ["<140/90", "60-100", "70-100 fasting", ">11 g/dL", "18.5-24.9"]
        })
        st.dataframe(indicators, use_container_width=True, hide_index=True)
    
    with tab2:
        col1, col2 = st.columns(2)
        with col1:
            st.metric("Blood Pressure", "118/76 mmHg", "Within normal range")
            st.metric("Heart Rate", "82 BPM", "Normal")
        with col2:
            st.metric("Blood Glucose", "96 mg/dL", "Fasting normal")
            st.metric("Temperature", "36.7°C", "Normal")
    
    with tab3:
        vitals_df = generate_vitals_data(30)
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=vitals_df['date'], y=vitals_df['systolic'], name='Systolic', line=dict(color='#EC0A7A')))
        fig.add_trace(go.Scatter(x=vitals_df['date'], y=vitals_df['diastolic'], name='Diastolic', line=dict(color='#C90062')))
        fig.update_layout(title='Blood Pressure Trend (30 days)', hovermode='x unified', height=400)
        st.plotly_chart(fig, use_container_width=True)

def vitals_page():
    """Detailed vitals monitoring"""
    st.markdown("<h1 style='color: #EC0A7A;'>Vital Signs Monitoring</h1>", unsafe_allow_html=True)
    
    time_range = st.selectbox("Time Range", ["Today", "7 Days", "30 Days", "3 Months"])
    
    days_map = {"Today": 1, "7 Days": 7, "30 Days": 30, "3 Months": 90}
    vitals_df = generate_vitals_data(days_map[time_range])
    
    # Vitals metrics
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Heart Rate", "82 BPM", "→ Normal")
    col2.metric("Blood Pressure", "118/76", "→ Normal")
    col3.metric("SpO2", "98%", "→ Normal")
    col4.metric("Temperature", "36.7°C", "→ Normal")
    
    st.markdown("---")
    
    # Charts
    col1, col2 = st.columns(2)
    
    with col1:
        fig_hr = go.Figure()
        fig_hr.add_trace(go.Scatter(x=vitals_df['date'], y=vitals_df['heart_rate'], mode='lines', name='Heart Rate', line=dict(color='#EC0A7A')))
        fig_hr.update_layout(title='Heart Rate Trend', height=350, hovermode='x unified')
        st.plotly_chart(fig_hr, use_container_width=True)
    
    with col2:
        fig_bp = go.Figure()
        fig_bp.add_trace(go.Scatter(x=vitals_df['date'], y=vitals_df['systolic'], name='Systolic', line=dict(color='#EC0A7A')))
        fig_bp.add_trace(go.Scatter(x=vitals_df['date'], y=vitals_df['diastolic'], name='Diastolic', line=dict(color='#C90062')))
        fig_bp.update_layout(title='Blood Pressure Trend', height=350, hovermode='x unified')
        st.plotly_chart(fig_bp, use_container_width=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        fig_glucose = go.Figure()
        fig_glucose.add_trace(go.Scatter(x=vitals_df['date'], y=vitals_df['blood_glucose'], mode='lines', name='Blood Glucose', line=dict(color='#FFA500'), fill='tozeroy', fillcolor='rgba(255, 165, 0, 0.1)'))
        fig_glucose.update_layout(title='Blood Glucose Trend', height=350, hovermode='x unified')
        st.plotly_chart(fig_glucose, use_container_width=True)
    
    with col2:
        fig_temp = go.Figure()
        fig_temp.add_trace(go.Scatter(x=vitals_df['date'], y=vitals_df['temperature'], mode='lines+markers', name='Temperature', line=dict(color='#FF6B6B')))
        fig_temp.update_layout(title='Temperature Trend', height=350, hovermode='x unified')
        st.plotly_chart(fig_temp, use_container_width=True)

def fetal_intelligence_page():
    """Fetal monitoring and intelligence"""
    st.markdown("<h1 style='color: #EC0A7A;'>Fetal Intelligence</h1>", unsafe_allow_html=True)
    
    # Baby profile
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col1:
        st.markdown(f"""
        <div class='baby-card-pink'>
            <h3 style='margin: 0; color: #C90062;'>{DEMO_BABY['name']}</h3>
            <p style='margin: 5px 0; font-size: 14px;'>👧 Female</p>
            <p style='margin: 5px 0; font-size: 14px;'><strong>{DEMO_PREGNANCY['current_week']} weeks</strong></p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div style='background: #F5F5F5; padding: 15px; border-radius: 8px;'>
            <h4 style='margin: 0 0 15px 0; color: #EC0A7A;'>Development Status</h4>
            <p style='margin: 5px 0; font-size: 13px;'>✓ <strong>Healthy development indicators</strong></p>
            <p style='margin: 5px 0; font-size: 13px;'>✓ All measurements within normal range</p>
            <p style='margin: 5px 0; font-size: 13px;'>✓ Growth tracking: On schedule</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div style='background: #E0F6FF; padding: 15px; border-radius: 8px;'>
            <h4 style='margin: 0 0 15px 0; color: #0288D1;'>Estimated Stats</h4>
            <p style='margin: 5px 0; font-size: 13px;'><strong>Weight:</strong> 1.1 kg</p>
            <p style='margin: 5px 0; font-size: 13px;'><strong>Length:</strong> 37.5 cm</p>
            <p style='margin: 5px 0; font-size: 13px;'><strong>Growth:</strong> 62nd %ile</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Fetal vitals
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Fetal Heart Rate", "142 BPM", "✓ Normal")
    col2.metric("Movement", "Active", "✓ Normal")
    col3.metric("Growth Percentile", "62%", "On track")
    col4.metric("Head Circumference", "26.5 cm", "Expected range")
    
    st.markdown("---")
    
    st.subheader("📈 Fetal Growth Charts")
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Estimated weight chart
        weeks = np.array([12, 14, 16, 18, 20, 22, 24, 26, 28])
        weights = np.array([50, 90, 140, 190, 300, 475, 600, 900, 1100])
        
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=weeks, y=weights, mode='lines+markers', name='Estimated Weight', line=dict(color='#EC0A7A', width=3)))
        fig.update_layout(title='Estimated Fetal Weight', xaxis_title='Gestational Week', yaxis_title='Weight (g)', height=300)
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        # Growth percentile chart
        fig = go.Figure(go.Indicator(
            mode="gauge+number+delta",
            value=62,
            domain={'x': [0, 1], 'y': [0, 1]},
            title={'text': "Growth Percentile"},
            delta={'reference': 50},
            gauge={
                'axis': {'range': [0, 100]},
                'bar': {'color': "#EC0A7A"},
                'steps': [
                    {'range': [0, 25], 'color': "#FFE4F0"},
                    {'range': [25, 50], 'color': "#FFD9ED"},
                    {'range': [50, 75], 'color': "#FCE4EF"},
                    {'range': [75, 100], 'color': "#EC0A7A"}
                ],
                'threshold': {
                    'line': {'color': "red", 'width': 4},
                    'thickness': 0.75,
                    'value': 90
                }
            }
        ))
        fig.update_layout(height=300)
        st.plotly_chart(fig, use_container_width=True)
    
    st.markdown("---")
    
    st.subheader("🫀 Fetal Monitoring History")
    fetal_history = pd.DataFrame({
        "Date": [(datetime.now() - timedelta(days=x)).strftime("%Y-%m-%d") for x in range(7)],
        "Heart Rate": [140 + np.random.randint(-5, 5) for _ in range(7)],
        "Movement": ["Active"] * 7,
        "Status": ["✓ Normal"] * 7,
    })
    st.dataframe(fetal_history, use_container_width=True, hide_index=True)

def medical_imaging_page():
    """Medical imaging and ultrasound analysis"""
    st.markdown("<h1 style='color: #EC0A7A;'>Medical Imaging & Ultrasound</h1>", unsafe_allow_html=True)
    
    tab1, tab2, tab3 = st.tabs(["📸 Image Viewer", "🤖 AI Analysis", "📋 Image History"])
    
    with tab1:
        st.subheader("Ultrasound Image Viewer")
        
        col1, col2 = st.columns([2, 1])
        
        with col1:
            # Create a placeholder ultrasound image (gradient)
            from PIL import Image, ImageDraw
            
            img = Image.new('RGB', (600, 400), color='black')
            draw = ImageDraw.Draw(img, 'RGBA')
            
            # Add some ultrasound-like patterns
            for i in range(0, 600, 20):
                for j in range(0, 400, 20):
                    brightness = int(100 + 100 * np.sin(i/100) * np.cos(j/100))
                    draw.rectangle([i, j, i+20, j+20], fill=(brightness, brightness//2, brightness//3, 200))
            
            # Add circles for fetal structures
            draw.ellipse([200, 150, 400, 250], outline=(200, 200, 200, 255), width=2)
            
            st.image(img, caption="Fetal Ultrasound - Week 28", use_container_width=True)
        
        with col2:
            st.markdown("""
            <div style='background: #F5F5F5; padding: 15px; border-radius: 8px;'>
                <h4 style='margin: 0 0 15px 0;'>Image Info</h4>
                <p style='margin: 5px 0; font-size: 12px;'><strong>ID:</strong> USG-2026-08-28-001</p>
                <p style='margin: 5px 0; font-size: 12px;'><strong>Date:</strong> Aug 28, 2026</p>
                <p style='margin: 5px 0; font-size: 12px;'><strong>GA:</strong> 28+3 weeks</p>
                <p style='margin: 5px 0; font-size: 12px;'><strong>Modality:</strong> 2D Ultrasound</p>
                <p style='margin: 5px 0; font-size: 12px;'><strong>Status:</strong> Analyzed</p>
            </div>
            """, unsafe_allow_html=True)
        
        st.markdown("---")
        st.markdown("<h4>Upload New Ultrasound Image</h4>", unsafe_allow_html=True)
        
        uploaded_file = st.file_uploader("Select image (PNG, JPG, JPEG)", type=["png", "jpg", "jpeg"])
        
        if uploaded_file:
            st.image(uploaded_file, caption="Uploaded Image", use_container_width=True)
            
            if st.button("Analyze with AI", use_container_width=True):
                with st.spinner("🔄 AI Analysis in progress..."):
                    progress_bar = st.progress(0)
                    for i in range(0, 101, 10):
                        progress_bar.progress(i)
                    
                    st.success("✓ Analysis Complete")
                    st.balloons()
    
    with tab2:
        st.subheader("AI Analysis Results")
        
        st.markdown("""
        <div style='background: #E8F5E9; border-left: 4px solid #4CAF50; padding: 15px; border-radius: 8px; margin-bottom: 20px;'>
            <h4 style='margin: 0 0 10px 0; color: #2E7D32;'>✓ Analysis Complete</h4>
            <p style='margin: 0; color: #388E3C;'><strong>Prediction:</strong> No significant abnormality detected</p>
            <p style='margin: 5px 0 0 0; color: #388E3C;'><strong>Confidence:</strong> 96.4%</p>
        </div>
        """, unsafe_allow_html=True)
        
        col1, col2, col3 = st.columns(3)
        categories = ["Brain", "Heart", "Spine", "Abdomen", "Limbs", "Facial Structure"]
        results = ["Normal", "Normal", "Normal", "Normal", "Normal", "Normal"]
        
        for i, (cat, res) in enumerate(zip(categories, results)):
            with st.columns(3)[i % 3]:
                st.markdown(f"""
                <div style='background: #FCE4EF; padding: 12px; border-radius: 8px; text-align: center;'>
                    <p style='margin: 0; font-size: 12px; color: #71717A;'>{cat}</p>
                    <p style='margin: 5px 0 0 0; font-weight: bold; color: #4CAF50;'>{res}</p>
                </div>
                """, unsafe_allow_html=True)
        
        st.markdown("---")
        
        st.markdown("""
        <div style='background: #FFF3E0; border-left: 4px solid #FF9800; padding: 15px; border-radius: 8px;'>
            <p style='margin: 0; font-size: 12px; color: #E65100;'><strong>⚠️ Disclaimer:</strong> AI-assisted screening only. Results must be reviewed by a qualified healthcare professional.</p>
        </div>
        """, unsafe_allow_html=True)
    
    with tab3:
        st.subheader("Recent Ultrasound Reports")
        
        imaging_history = pd.DataFrame({
            "Date": ["2026-08-28", "2026-07-30", "2026-06-28"],
            "GA (weeks)": ["28+3", "24+2", "20+1"],
            "Modality": ["2D Ultrasound", "2D Ultrasound", "3D Ultrasound"],
            "Status": ["Analyzed", "Analyzed", "Analyzed"],
            "Result": ["Normal", "Normal", "Normal"],
        })
        st.dataframe(imaging_history, use_container_width=True, hide_index=True)

def ai_predictions_page():
    """AI-powered pregnancy risk predictions"""
    st.markdown("<h1 style='color: #EC0A7A;'>Pregnancy Risk Intelligence</h1>", unsafe_allow_html=True)
    
    # Overall risk summary
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown(f"""
        <div style='background: linear-gradient(135deg, #E8F5E9 0%, #F1F8E9 100%); border-radius: 12px; padding: 20px; text-align: center;'>
            <p style='margin: 0; color: #71717A; font-size: 12px;'>OVERALL RISK</p>
            <h1 style='margin: 10px 0 0 0; color: #4CAF50; font-size: 36px;'>LOW</h1>
            <p style='margin: 10px 0 0 0; font-size: 12px; color: #71717A;'>Risk Score: 8/100</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div style='background: linear-gradient(135deg, #E3F2FD 0%, #F3E5F5 100%); border-radius: 12px; padding: 20px; text-align: center;'>
            <p style='margin: 0; color: #71717A; font-size: 12px;'>MODEL CONFIDENCE</p>
            <h1 style='margin: 10px 0 0 0; color: #1976D2; font-size: 36px;'>94%</h1>
            <p style='margin: 10px 0 0 0; font-size: 12px; color: #71717A;'>Based on 47 parameters</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div style='background: linear-gradient(135deg, #F3E5F5 0%, #FCE4EF 100%); border-radius: 12px; padding: 20px; text-align: center;'>
            <p style='margin: 0; color: #71717A; font-size: 12px;'>TREND</p>
            <h1 style='margin: 10px 0 0 0; color: #4CAF50; font-size: 36px;'>Stable</h1>
            <p style='margin: 10px 0 0 0; font-size: 12px; color: #71717A;'>↓ -2.1% vs last week</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    st.subheader("Risk Stratification")
    
    # Risk categories
    for condition, data in DEMO_RISK_PREDICTIONS.items():
        risk_level = data['risk']
        status = data['status']
        trend = data['trend']
        
        # Color based on risk
        if risk_level < 15:
            color = "#4CAF50"
            bg_color = "#E8F5E9"
        elif risk_level < 30:
            color = "#FFA500"
            bg_color = "#FFF3E0"
        else:
            color = "#FF6B6B"
            bg_color = "#FFEBEE"
        
        col1, col2, col3, col4 = st.columns([2, 1, 1, 1])
        
        with col1:
            st.markdown(f"<p style='margin: 0; font-weight: bold;'>{condition}</p>", unsafe_allow_html=True)
        with col2:
            st.markdown(f"<p style='margin: 0; color: {color};'><strong>{risk_level}%</strong></p>", unsafe_allow_html=True)
        with col3:
            st.markdown(f"<p style='margin: 0; font-size: 12px; color: #71717A;'>{status}</p>", unsafe_allow_html=True)
        with col4:
            st.markdown(f"<p style='margin: 0; font-size: 12px; color: {color};'>{trend}</p>", unsafe_allow_html=True)
    
    st.markdown("---")
    
    st.subheader("AI Explanation")
    st.info(
        "Based on current maternal vitals, pregnancy history, and recent measurements, "
        "the model currently identifies a low-risk profile. All key indicators remain within normal ranges. "
        "Continue regular prenatal monitoring and follow up as scheduled."
    )
    
    st.warning(
        "⚠️ **Disclaimer:** This is an AI-assisted decision-support prediction and not a medical diagnosis. "
        "Please consult with your healthcare provider for medical decisions."
    )

def appointments_page():
    """Appointments management"""
    st.markdown("<h1 style='color: #EC0A7A;'>Appointments</h1>", unsafe_allow_html=True)
    
    tab1, tab2 = st.tabs(["📅 Upcoming", "✅ History"])
    
    with tab1:
        st.subheader("Upcoming Appointments")
        
        upcoming = [a for a in DEMO_APPOINTMENTS if a['status'] == 'Upcoming']
        
        for appt in upcoming:
            col1, col2, col3 = st.columns([2, 1, 1])
            
            with col1:
                st.markdown(f"""
                <div style='background: #FCE4EF; padding: 15px; border-radius: 8px; border-left: 4px solid #EC0A7A;'>
                    <p style='margin: 0; font-weight: bold; color: #EC0A7A;'>Dr. {appt['doctor']}</p>
                    <p style='margin: 5px 0 0 0; font-size: 12px; color: #71717A;'>{appt['specialty']}</p>
                    <p style='margin: 5px 0 0 0; font-size: 12px; color: #71717A;'>{appt['type']}</p>
                    <p style='margin: 8px 0 0 0; font-size: 11px; background: #FCE4EF; padding: 5px 8px; border-radius: 4px; width: fit-content;'>
                        📅 {appt['date']} at {appt['time']}
                    </p>
                </div>
                """, unsafe_allow_html=True)
            
            with col2:
                if st.button("📞 Join", key=f"join_{appt['id']}", use_container_width=True):
                    st.success(f"Joining consultation with Dr. {appt['doctor']}...")
            
            with col3:
                if st.button("📋 Reschedule", key=f"reschedule_{appt['id']}", use_container_width=True):
                    st.info("Reschedule feature coming soon")
    
    with tab2:
        st.subheader("Appointment History")
        
        completed = [a for a in DEMO_APPOINTMENTS if a['status'] == 'Completed']
        
        for appt in completed:
            st.markdown(f"""
            <div style='background: #F5F5F5; padding: 12px; border-radius: 8px; margin-bottom: 8px;'>
                <p style='margin: 0; font-weight: bold;'>Dr. {appt['doctor']}</p>
                <p style='margin: 5px 0; font-size: 12px; color: #71717A;'>{appt['type']}</p>
                <p style='margin: 5px 0 0 0; font-size: 12px; color: #4CAF50;'>✓ {appt['date']}</p>
            </div>
            """, unsafe_allow_html=True)

def care_timeline_page():
    """Care timeline visualization"""
    st.markdown("<h1 style='color: #EC0A7A;'>Care Timeline</h1>", unsafe_allow_html=True)
    
    st.subheader("Pregnancy Journey")
    
    # Timeline visualization
    for item in DEMO_CARE_TIMELINE:
        if item['status'] == 'completed':
            icon = "✅"
            color = "#4CAF50"
            bg = "#E8F5E9"
        elif item['status'] == 'current':
            icon = "●"
            color = "#EC0A7A"
            bg = "#FCE4EF"
        else:
            icon = "○"
            color = "#BDBDBD"
            bg = "#F5F5F5"
        
        st.markdown(f"""
        <div style='background: {bg}; padding: 15px; border-radius: 8px; border-left: 4px solid {color}; margin-bottom: 10px;'>
            <p style='margin: 0;'><span style='color: {color}; font-weight: bold; font-size: 16px;'>{icon}</span> 
            <strong>Week {item['week']}</strong> • {item['event']}</p>
        </div>
        """, unsafe_allow_html=True)

def medications_page():
    """Medication management"""
    st.markdown("<h1 style='color: #EC0A7A;'>Medications</h1>", unsafe_allow_html=True)
    
    st.subheader("Current Medications")
    
    col1, col2, col3 = st.columns(3)
    
    for i, med in enumerate(DEMO_MEDICATIONS):
        with st.columns(3)[i % 3]:
            status_color = "#4CAF50" if med['status'] == "Taken" else "#FFA500"
            
            st.markdown(f"""
            <div style='background: #FCE4EF; padding: 15px; border-radius: 8px; border: 1px solid #E8D5E0;'>
                <h4 style='margin: 0 0 10px 0; color: #EC0A7A;'>{med['name']}</h4>
                <p style='margin: 5px 0; font-size: 12px;'><strong>{med['dosage']}</strong></p>
                <p style='margin: 5px 0; font-size: 12px; color: #71717A;'>{med['frequency']}</p>
                <p style='margin: 5px 0; font-size: 12px; color: #71717A;'>⏰ {med['time']}</p>
                <p style='margin: 10px 0 0 0; padding: 5px 8px; background: {status_color}22; color: {status_color}; border-radius: 4px; font-size: 12px; font-weight: bold;'>
                    {med['status']}
                </p>
                <p style='margin: 5px 0 0 0; font-size: 11px; color: #71717A;'>Adherence: {med['adherence']}%</p>
            </div>
            """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    st.subheader("Medication Adherence")
    
    adherence_data = pd.DataFrame({
        "Medication": [m['name'] for m in DEMO_MEDICATIONS],
        "Adherence": [m['adherence'] for m in DEMO_MEDICATIONS],
    })
    
    fig = go.Figure(data=[
        go.Bar(x=adherence_data['Medication'], y=adherence_data['Adherence'], marker_color='#EC0A7A')
    ])
    fig.update_layout(title='Medication Adherence Rate', yaxis_title='Adherence %', height=350)
    st.plotly_chart(fig, use_container_width=True)

def vaccinations_page():
    """Vaccination and immunization tracker"""
    st.markdown("<h1 style='color: #EC0A7A;'>Baby Immunization Journey</h1>", unsafe_allow_html=True)
    
    # Baby profile
    if st.session_state.baby_gender == "female":
        baby_name = "Lumi"
        baby_color = "Baby Pink"
        color_class = "baby-card-pink"
    else:
        baby_name = "Arjun"
        baby_color = "Baby Blue"
        color_class = "baby-card-blue"
    
    st.markdown(f"""
    <div class='{color_class}'>
        <h3 style='margin: 0;'>{baby_name}'s Immunization</h3>
        <p style='margin: 5px 0; font-size: 12px;'>👶 {st.session_state.baby_gender.capitalize()} • Theme: {baby_color}</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    st.subheader("Vaccination Timeline")
    
    for vac in DEMO_VACCINATIONS:
        if vac['status'] == 'Completed':
            icon = "✅"
            color = "#4CAF50"
            bg = "#E8F5E9"
        elif vac['status'] == 'Upcoming':
            icon = "📅"
            color = "#FFA500"
            bg = "#FFF3E0"
        else:
            icon = "⏳"
            color = "#BDBDBD"
            bg = "#F5F5F5"
        
        col1, col2, col3, col4 = st.columns([1, 2, 1, 1])
        
        with col1:
            st.markdown(f"<p style='margin: 0; font-size: 20px;'>{icon}</p>", unsafe_allow_html=True)
        with col2:
            st.markdown(f"""
            <div>
                <p style='margin: 0; font-weight: bold;'>{vac['name']}</p>
                <p style='margin: 5px 0 0 0; font-size: 11px; color: #71717A;'>Due: {vac['date']}</p>
            </div>
            """, unsafe_allow_html=True)
        with col3:
            st.markdown(f"<p style='margin: 0; color: {color}; font-weight: bold;'>{vac['status']}</p>", unsafe_allow_html=True)
        with col4:
            if vac['due']:
                st.button("🔔 Remind", key=f"vac_{vac['name']}", use_container_width=True)

def followup_page():
    """Follow-up care"""
    st.markdown("<h1 style='color: #EC0A7A;'>Follow-up Care</h1>", unsafe_allow_html=True)
    
    st.subheader("Next Care Actions")
    
    for action in DEMO_FOLLOW_UP_ACTIONS:
        priority_color = "#FF6B6B" if action['priority'] == "Urgent" else "#FFA500" if action['priority'] == "Important" else "#4CAF50"
        bg_color = priority_color + "22"
        
        col1, col2 = st.columns([3, 1])
        
        with col1:
            st.markdown(f"""
            <div style='background: {bg_color}; border-left: 4px solid {priority_color}; padding: 15px; border-radius: 8px;'>
                <p style='margin: 0; font-weight: bold; color: {priority_color};'>{action['action']}</p>
                <p style='margin: 5px 0 0 0; font-size: 12px; color: #71717A;'>Due: {action['due']} • Priority: {action['priority']}</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            if st.button("✓ Complete", key=f"action_{action['id']}", use_container_width=True):
                st.success("Action marked as complete!")

def reports_page():
    """Medical reports center"""
    st.markdown("<h1 style='color: #EC0A7A;'>Medical Reports</h1>", unsafe_allow_html=True)
    
    tab1, tab2 = st.tabs(["📋 All Reports", "🔍 Filter"])
    
    with tab1:
        st.subheader("Your Reports")
        
        for report in DEMO_REPORTS:
            col1, col2, col3, col4 = st.columns([2, 1, 1, 1])
            
            with col1:
                st.markdown(f"""
                <div style='background: #FCE4EF; padding: 12px; border-radius: 8px;'>
                    <p style='margin: 0; font-weight: bold;'>{report['title']}</p>
                    <p style='margin: 5px 0 0 0; font-size: 11px; color: #71717A;'>Dr. {report['doctor']}</p>
                </div>
                """, unsafe_allow_html=True)
            
            with col2:
                st.markdown(f"<p style='margin: 0; font-size: 12px; color: #71717A;'>{report['date']}</p>", unsafe_allow_html=True)
            
            with col3:
                st.button("👁️ View", key=f"view_{report['id']}", use_container_width=True)
            
            with col4:
                st.button("⬇️ Download", key=f"download_{report['id']}", use_container_width=True)
    
    with tab2:
        st.subheader("Filter Reports")
        
        category = st.multiselect("Category", ["All", "Maternal", "Fetal", "Neonatal", "Laboratory", "AI"], default="All")
        
        if category:
            st.info(f"Showing reports for: {', '.join(category)}")

def notifications_page():
    """Notifications center"""
    st.markdown("<h1 style='color: #EC0A7A;'>Notifications</h1>", unsafe_allow_html=True)
    
    st.subheader("Recent Notifications")
    
    for notif in DEMO_NOTIFICATIONS:
        read_style = "opacity: 0.6;" if notif['read'] else ""
        
        st.markdown(f"""
        <div style='background: #FCE4EF; padding: 15px; border-radius: 8px; margin-bottom: 10px; border-left: 4px solid #EC0A7A; {read_style}'>
            <div style='display: flex; justify-content: space-between; align-items: start;'>
                <div style='flex: 1;'>
                    <p style='margin: 0; font-weight: bold; color: #EC0A7A;'>{notif['type']}</p>
                    <p style='margin: 5px 0 0 0; color: #27272A;'>{notif['message']}</p>
                    <p style='margin: 10px 0 0 0; font-size: 11px; color: #71717A;'>{notif['date']}</p>
                </div>
                <div>
                    <span style='background: #EC0A7A; color: white; padding: 4px 8px; border-radius: 12px; font-size: 11px;'>{notif['type']}</span>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

def neonatal_page():
    """Neonatal care dashboard"""
    st.markdown(f"<h1 style='color: #EC0A7A;'>Welcome to your little one's world</h1>", unsafe_allow_html=True)
    
    # Baby profile based on gender
    if st.session_state.baby_gender == "female":
        baby_name = "Lumi"
        color_class = "baby-card-pink"
    else:
        baby_name = "Arjun"
        color_class = "baby-card-blue"
    
    st.markdown(f"""
    <div class='{color_class}'>
        <h2 style='margin: 0;'>{baby_name} 👶</h2>
        <p style='margin: 5px 0; font-size: 14px;'>Age: {DEMO_NEONATAL['age_days']} days • Born healthy</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Vital signs
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Weight", f"{DEMO_NEONATAL['weight']} kg", "On track")
    col2.metric("Height", f"{DEMO_NEONATAL['height']} cm", "Healthy")
    col3.metric("Head Circumference", f"{DEMO_NEONATAL['head_circumference']} cm", "Normal")
    col4.metric("Temperature", f"{DEMO_NEONATAL['temperature']}°C", "Normal")
    
    st.markdown("---")
    
    # Real-time monitoring
    st.subheader("🔴 Real-time Baby Monitoring")
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Baby heart rate
        fetal_df = generate_fetal_hr_data(24)
        fig_hr = go.Figure()
        fig_hr.add_trace(go.Scatter(
            x=fetal_df['time'],
            y=fetal_df['fetal_hr'],
            mode='lines+markers',
            name='Heart Rate',
            line=dict(color='#87CEEB', width=3),
            fill='tozeroy',
            fillcolor='rgba(135, 206, 235, 0.1)',
        ))
        fig_hr.update_layout(title='Heart Rate (24h)', height=300)
        st.plotly_chart(fig_hr, use_container_width=True)
    
    with col2:
        # Vitals summary
        vitals_df = generate_vitals_data(24)
        fig_temp = go.Figure()
        fig_temp.add_trace(go.Scatter(x=vitals_df['date'], y=vitals_df['temperature'], mode='lines', name='Temperature', line=dict(color='#FF6B6B')))
        fig_temp.update_layout(title='Temperature (24h)', height=300)
        st.plotly_chart(fig_temp, use_container_width=True)

def ai_assistant_page():
    """AI care assistant"""
    st.markdown("<h1 style='color: #EC0A7A;'>Umbilica Care AI</h1>", unsafe_allow_html=True)
    
    st.subheader("Your AI-Powered Healthcare Assistant")
    
    st.info("Ask me about your pregnancy, baby care, vaccinations, medications, and more!")
    
    # Example prompts
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("📊 How is my baby's growth?", use_container_width=True):
            st.markdown("""
            Your baby is growing beautifully! At week 28, the estimated weight is 1.1 kg, 
            which is right on track for gestational age. The growth percentile is at 62%, 
            indicating healthy development.
            """)
    
    with col2:
        if st.button("💉 What vaccinations are coming up?", use_container_width=True):
            st.markdown("""
            After delivery, your baby will receive BCG and Hepatitis B at birth. 
            At 6 weeks, DPT, Rotavirus, Pneumococcal, and Polio vaccines are due. 
            At 9-12 months, Measles vaccination will be administered.
            """)
    
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("🤰 Show my pregnancy risk summary", use_container_width=True):
            st.markdown("""
            Your overall pregnancy risk is LOW (8/100). All major risk factors are within 
            normal ranges: Pre-eclampsia (12%), Gestational Diabetes (18%), Preterm Birth (9%), 
            and Anemia (14%). Continue regular prenatal care.
            """)
    
    with col2:
        if st.button("📋 What should I prepare for delivery?", use_container_width=True):
            st.markdown("""
            You're in your third trimester. Key preparations:
            - Pack hospital bag with essentials
            - Complete prenatal classes
            - Discuss delivery plan with your doctor
            - Arrange childcare support
            - Know labor warning signs
            """)
    
    st.markdown("---")
    
    st.subheader("Chat with AI Assistant")
    
    user_question = st.text_input("Ask a question about your healthcare:")
    
    if user_question:
        st.markdown(f"""
        <div style='background: #FCE4EF; padding: 12px; border-radius: 8px; margin: 10px 0;'>
            <p style='margin: 0; font-weight: bold; color: #EC0A7A;'>You: {user_question}</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Simulate AI response
        responses = {
            "pregnancy": "Your current pregnancy is progressing well. You're at week 28 with a low-risk profile. Continue regular check-ups and follow your doctor's recommendations.",
            "baby": "Your baby is developing beautifully with healthy growth indicators. All measurements are within normal ranges for your gestational age.",
            "medication": "Your medications (Folic Acid, Iron, Calcium) are important for your health and baby's development. Maintain good adherence for best results.",
            "appointment": "Your next appointment is scheduled for September 4, 2026 at 10:30 AM with Dr. Meera Sharma for prenatal consultation.",
        }
        
        for key in responses.keys():
            if key in user_question.lower():
                st.markdown(f"""
                <div style='background: #E8F5E9; padding: 12px; border-radius: 8px; margin: 10px 0;'>
                    <p style='margin: 0; font-weight: bold; color: #4CAF50;'>Umbilica AI: {responses[key]}</p>
                </div>
                """, unsafe_allow_html=True)
                break
        else:
            st.markdown("""
            <div style='background: #E8F5E9; padding: 12px; border-radius: 8px; margin: 10px 0;'>
                <p style='margin: 0; font-weight: bold; color: #4CAF50;'>Umbilica AI: I'm here to help with your healthcare questions. Feel free to ask about your pregnancy, baby, medications, appointments, or any health concerns.</p>
            </div>
            """, unsafe_allow_html=True)
    
    st.warning(
        "⚠️ **Note:** AI responses are for informational purposes only. Always consult your healthcare professional for medical decisions."
    )

def profile_page():
    """User profile"""
    st.markdown("<h1 style='color: #EC0A7A;'>My Profile</h1>", unsafe_allow_html=True)
    
    tab1, tab2, tab3 = st.tabs(["👩 Mother Profile", "👶 Baby Profile", "📞 Emergency Contacts"])
    
    with tab1:
        st.subheader("Maternal Information")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.write("**Name:**", DEMO_MOTHER['name'])
            st.write("**Age:**", f"{DEMO_MOTHER['age']} years")
            st.write("**Blood Group:**", DEMO_MOTHER['blood_group'])
            st.write("**Height:**", DEMO_MOTHER['height'])
        
        with col2:
            st.write("**Weight:**", DEMO_MOTHER['weight'])
            st.write("**Email:**", DEMO_MOTHER['email'])
            st.write("**Phone:**", DEMO_MOTHER['phone'])
        
        st.markdown("---")
        
        st.subheader("Pregnancy Information")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.write("**Current Week:**", DEMO_PREGNANCY['current_week'])
            st.write("**Trimester:**", DEMO_PREGNANCY['trimester'])
            st.write("**Expected Delivery:**", DEMO_PREGNANCY['edd'].strftime("%B %d, %Y"))
        
        with col2:
            st.write("**First Pregnancy:**", "No" if DEMO_PREGNANCY['first_pregnancy'] else "No")
            st.write("**Previous Pregnancies:**", DEMO_PREGNANCY['previous_pregnancies'])
            st.write("**Previous Complications:**", "No")
    
    with tab2:
        st.subheader("Baby Information")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.write("**Baby Name:**", DEMO_BABY['name'])
            st.write("**Gender:**", DEMO_BABY['gender'].capitalize())
        
        with col2:
            st.write("**Estimated Weight:**", f"{DEMO_BABY['estimated_weight']} kg")
            st.write("**Growth Percentile:**", f"{DEMO_BABY['growth_percentile']}%")
    
    with tab3:
        st.subheader("Emergency Contacts")
        
        st.write("**Primary Contact:**", DEMO_MOTHER['emergency_contact'])
        st.write("**Phone:**", DEMO_MOTHER['emergency_phone'])
        
        st.info("Emergency contacts are used in case of urgent medical situations.")

def settings_page():
    """Application settings"""
    st.markdown("<h1 style='color: #EC0A7A;'>Settings</h1>", unsafe_allow_html=True)
    
    tab1, tab2, tab3, tab4 = st.tabs(["👶 Baby Theme", "🔔 Notifications", "🔒 Privacy", "🎨 Theme"])
    
    with tab1:
        st.subheader("Baby Gender & Theme")
        
        st.write("Customize your baby-related dashboard theme:")
        
        col1, col2 = st.columns(2)
        
        with col1:
            if st.button("👧 Female Baby (Baby Pink)", use_container_width=True, type="secondary" if st.session_state.baby_gender != "female" else "primary"):
                st.session_state.baby_gender = "female"
                st.success("✓ Theme updated to Baby Pink")
                st.rerun()
        
        with col2:
            if st.button("👦 Male Baby (Baby Blue)", use_container_width=True, type="secondary" if st.session_state.baby_gender != "male" else "primary"):
                st.session_state.baby_gender = "male"
                st.success("✓ Theme updated to Baby Blue")
                st.rerun()
        
        st.markdown("---")
        
        st.info(f"Current setting: {st.session_state.baby_gender.capitalize()} Baby")
    
    with tab2:
        st.subheader("Notification Preferences")
        
        st.write("Choose what notifications you'd like to receive:")
        
        st.checkbox("Appointment Reminders", value=True)
        st.checkbox("Medication Reminders", value=True)
        st.checkbox("Vaccination Alerts", value=True)
        st.checkbox("Health Tips", value=True)
        st.checkbox("Lab Results", value=True)
        
        if st.button("Save Preferences", use_container_width=True):
            st.success("✓ Notification preferences saved")
    
    with tab3:
        st.subheader("Privacy & Data")
        
        st.write("Your health data is encrypted and secure.")
        st.info("All medical information is stored securely and complies with healthcare privacy regulations.")
        
        st.write("**Data Access:**")
        st.write("- Your doctor can access your records with your consent")
        st.write("- AI analysis is performed locally on your device")
        st.write("- No data is shared with third parties")
    
    with tab4:
        st.subheader("Theme Settings")
        
        st.write("Application theme: Light Mode (Premium Pink & White)")
        st.info("The application uses a premium maternal healthcare color scheme optimized for comfortable viewing.")
        
        if st.button("🚪 Reset Demo Data", use_container_width=True):
            st.success("✓ Demo data reset complete")

# Main entry point
if __name__ == "__main__":
    if not st.session_state.authenticated:
        login_page()
    else:
        main_app()
