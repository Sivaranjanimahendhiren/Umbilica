"""UMBILICA Configuration and Demo Data"""

import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Color Palettes
PRIMARY_PINK = "#EC0A7A"
DEEP_PINK = "#C90062"
SOFT_PINK = "#FCE4EF"
BLUSH = "#FFF4F8"
WHITE = "#FFFFFF"
TEXT_DARK = "#27272A"
TEXT_SECONDARY = "#71717A"

BABY_PINK_PRIMARY = "#FFB3D9"
BABY_PINK_LIGHT = "#FFE4F0"

BABY_BLUE_PRIMARY = "#87CEEB"
BABY_BLUE_LIGHT = "#E0F6FF"

# Demo User Data
DEMO_MOTHER = {
    "name": "Ananya Rao",
    "age": 27,
    "blood_group": "O+",
    "height": "5'6\"",
    "weight": "62 kg",
    "email": "demo@umbilica.ai",
    "phone": "+91 9876543210",
    "emergency_contact": "Rahul Rao",
    "emergency_phone": "+91 9876543211",
}

DEMO_PREGNANCY = {
    "current_week": 28,
    "trimester": "Third",
    "edd": datetime(2026, 11, 12),
    "first_pregnancy": False,
    "previous_pregnancies": 1,
    "previous_complications": False,
}

DEMO_BABY = {
    "name": "Lumi",
    "gender": "female",  # Can be "male" or "female"
    "estimated_weight": 1.1,
    "estimated_height": 37.5,
    "head_circumference": 26.5,
    "growth_percentile": 62,
}

DEMO_VITALS_LATEST = {
    "heart_rate": 82,
    "blood_pressure": "118/76",
    "spo2": 98,
    "temperature": 36.7,
    "blood_glucose": 96,
    "hemoglobin": 11.2,
    "bmi": 22.4,
}

DEMO_FETAL_VITALS = {
    "heart_rate": 142,
    "movement": "Normal",
    "growth_status": "On track",
}

DEMO_HEALTH_SCORE = 92

DEMO_AI_RISK_SCORE = 8  # percentage

# Generate demo vitals time series data
def generate_vitals_data(days=30):
    """Generate realistic demo vitals data"""
    dates = [datetime.now() - timedelta(days=x) for x in range(days)]
    dates = sorted(dates)
    
    data = {
        "date": dates,
        "heart_rate": [82 + np.random.randint(-5, 5) for _ in dates],
        "systolic": [118 + np.random.randint(-3, 3) for _ in dates],
        "diastolic": [76 + np.random.randint(-3, 3) for _ in dates],
        "spo2": [98 + np.random.randint(-1, 1) for _ in dates],
        "temperature": [36.7 + np.random.uniform(-0.3, 0.3) for _ in dates],
        "blood_glucose": [96 + np.random.randint(-5, 10) for _ in dates],
    }
    return pd.DataFrame(data)

# Fetal heart rate data
def generate_fetal_hr_data(hours=24):
    """Generate fetal heart rate data"""
    times = [datetime.now() - timedelta(hours=x) for x in range(hours)]
    times = sorted(times)
    
    data = {
        "time": times,
        "fetal_hr": [142 + np.random.randint(-8, 8) for _ in times],
        "fetal_movement": [1 if np.random.random() > 0.3 else 0 for _ in times],
    }
    return pd.DataFrame(data)

# Risk prediction data
DEMO_RISK_PREDICTIONS = {
    "Pre-eclampsia": {"risk": 12, "status": "Low", "trend": "↑ +2%"},
    "Gestational Diabetes": {"risk": 18, "status": "Low", "trend": "↓ -3%"},
    "Preterm Birth": {"risk": 9, "status": "Low", "trend": "→ 0%"},
    "Anemia": {"risk": 14, "status": "Low", "trend": "↓ -1%"},
    "Hypertension": {"risk": 8, "status": "Low", "trend": "↑ +1%"},
    "Fetal Growth Restriction": {"risk": 11, "status": "Low", "trend": "→ 0%"},
}

# Demo appointments
DEMO_APPOINTMENTS = [
    {
        "id": 1,
        "doctor": "Dr. Meera Sharma",
        "specialty": "Obstetrician",
        "date": (datetime.now() + timedelta(days=6)).strftime("%Y-%m-%d"),
        "time": "10:30 AM",
        "type": "Prenatal Consultation",
        "status": "Upcoming",
    },
    {
        "id": 2,
        "doctor": "Dr. Rajesh Kumar",
        "specialty": "Fetal Specialist",
        "date": (datetime.now() + timedelta(days=14)).strftime("%Y-%m-%d"),
        "time": "2:00 PM",
        "type": "Fetal Growth Scan",
        "status": "Upcoming",
    },
    {
        "id": 3,
        "doctor": "Dr. Meera Sharma",
        "specialty": "Obstetrician",
        "date": (datetime.now() - timedelta(days=7)).strftime("%Y-%m-%d"),
        "time": "11:00 AM",
        "type": "Routine Check-up",
        "status": "Completed",
    },
]

# Demo medications
DEMO_MEDICATIONS = [
    {
        "name": "Folic Acid",
        "dosage": "400 mcg",
        "frequency": "Once daily",
        "time": "8:00 AM",
        "status": "Taken",
        "adherence": 95,
    },
    {
        "name": "Iron Supplement",
        "dosage": "300 mg",
        "frequency": "Once daily",
        "time": "9:00 PM",
        "status": "Pending",
        "adherence": 88,
    },
    {
        "name": "Calcium",
        "dosage": "1000 mg",
        "frequency": "Once daily",
        "time": "1:00 PM",
        "status": "Taken",
        "adherence": 92,
    },
]

# Demo vaccinations
DEMO_VACCINATIONS = [
    {"name": "BCG", "status": "Completed", "date": "0-7 days", "due": False},
    {"name": "Hepatitis B", "status": "Completed", "date": "0-7 days", "due": False},
    {"name": "OPV", "status": "Completed", "date": "6 weeks", "due": False},
    {"name": "DPT", "status": "Upcoming", "date": "6 weeks", "due": True},
    {"name": "Rotavirus", "status": "Upcoming", "date": "6 weeks", "due": True},
    {"name": "Pneumococcal", "status": "Upcoming", "date": "6 weeks", "due": True},
    {"name": "Measles", "status": "Pending", "date": "9-12 months", "due": False},
]

# Demo care timeline
DEMO_CARE_TIMELINE = [
    {"week": 12, "event": "First Trimester Screening", "status": "completed"},
    {"week": 16, "event": "Routine Check-up", "status": "completed"},
    {"week": 20, "event": "Anomaly Scan", "status": "completed"},
    {"week": 24, "event": "Glucose Screening", "status": "completed"},
    {"week": 28, "event": "Current Visit", "status": "current"},
    {"week": 32, "event": "Growth Scan", "status": "upcoming"},
    {"week": 36, "event": "Final Prenatal Assessment", "status": "upcoming"},
    {"week": 40, "event": "Expected Delivery", "status": "upcoming"},
]

# Demo reports
DEMO_REPORTS = [
    {
        "id": 1,
        "title": "Fetal Ultrasound Report",
        "date": "2026-08-25",
        "doctor": "Dr. Rajesh Kumar",
        "category": "Fetal",
        "status": "Available",
    },
    {
        "id": 2,
        "title": "Blood Test Report",
        "date": "2026-08-22",
        "doctor": "Lab",
        "category": "Laboratory",
        "status": "Available",
    },
    {
        "id": 3,
        "title": "Pregnancy Risk Assessment",
        "date": "2026-08-28",
        "doctor": "AI System",
        "category": "AI",
        "status": "Available",
    },
]

# Demo notifications
DEMO_NOTIFICATIONS = [
    {
        "id": 1,
        "message": "Your appointment with Dr. Meera Sharma is tomorrow at 10:30 AM",
        "type": "Appointment",
        "date": datetime.now().strftime("%Y-%m-%d %H:%M"),
        "read": False,
    },
    {
        "id": 2,
        "message": "Baby vaccination is due in 3 days",
        "type": "Vaccination",
        "date": (datetime.now() - timedelta(hours=2)).strftime("%Y-%m-%d %H:%M"),
        "read": False,
    },
    {
        "id": 3,
        "message": "Your latest fetal monitoring results are available",
        "type": "Lab Test",
        "date": (datetime.now() - timedelta(days=1)).strftime("%Y-%m-%d %H:%M"),
        "read": True,
    },
]

# Demo follow-up actions
DEMO_FOLLOW_UP_ACTIONS = [
    {
        "id": 1,
        "action": "Schedule blood test",
        "priority": "Important",
        "due": "3 days",
    },
    {
        "id": 2,
        "action": "Complete hydration goal",
        "priority": "Routine",
        "due": "Today",
    },
    {
        "id": 3,
        "action": "Review ultrasound report",
        "priority": "Important",
        "due": "1 day",
    },
    {
        "id": 4,
        "action": "Prenatal consultation",
        "priority": "Urgent",
        "due": "6 days",
    },
]

# Neonatal demo data
DEMO_NEONATAL = {
    "age_days": 18,
    "weight": 3.4,
    "height": 51,
    "head_circumference": 35,
    "temperature": 36.8,
    "heart_rate": 138,
    "spo2": 98,
    "respiratory_rate": 42,
}

# Baby feeding data
DEMO_FEEDING = [
    {"time": "06:30", "type": "Breastfeeding", "duration": 15, "quantity": None},
    {"time": "09:45", "type": "Formula", "duration": None, "quantity": 120},
    {"time": "13:20", "type": "Breastfeeding", "duration": 18, "quantity": None},
    {"time": "16:00", "type": "Breastfeeding", "duration": 16, "quantity": None},
    {"time": "19:30", "type": "Formula", "duration": None, "quantity": 100},
]

# Baby sleep data
DEMO_SLEEP = {
    "total_sleep": 16.5,
    "night_sleep": 8.2,
    "day_naps": 8.3,
    "wake_periods": 5,
}
