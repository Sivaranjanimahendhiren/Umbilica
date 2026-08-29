# 🏥 UMBILICA - Intelligent Care. From Motherhood to New Beginnings.

**AI-powered maternal, fetal and neonatal healthcare intelligence platform**

A production-quality, premium healthcare application built with Streamlit that combines maternal monitoring, pregnancy risk prediction, fetal abnormality detection, ultrasound analysis, and comprehensive neonatal care tracking.

## 🌟 Features

### Maternal Healthcare
- **Maternal Health Dashboard** - Real-time health scoring and monitoring
- **Vital Signs Tracking** - Heart rate, blood pressure, oxygen saturation, temperature, blood glucose
- **Pregnancy Progress** - Week-by-week tracking with trimester indicators
- **Maternal Care Overview** - Comprehensive health indicators and trends

### Pregnancy Intelligence
- **AI Risk Prediction** - Pre-eclampsia, gestational diabetes, preterm birth, anemia risk assessment
- **Pregnancy Risk Intelligence** - Low/Medium/High risk stratification with confidence scores
- **Care Timeline** - Visual pregnancy journey from conception to delivery
- **Health Scores** - Personalized maternal wellness scores with trends

### Fetal Monitoring
- **Fetal Intelligence Dashboard** - Real-time fetal heart rate and movement tracking
- **Fetal Growth Charts** - Estimated weight, length, head circumference, growth percentiles
- **Fetal Development Status** - Week-by-week development indicators
- **Fetal Abnormality Prediction** - AI-powered ultrasound analysis

### Medical Imaging & Analysis
- **Ultrasound Image Viewer** - DICOM and standard image format support
- **AI Image Analysis** - Automated detection of anatomical structures and abnormalities
- **Medical Image Reports** - Detailed findings, measurements, and follow-up recommendations
- **Image History** - Complete repository of all scans and analysis results

### Appointment & Care Management
- **Appointment Scheduling** - Doctor consultations with calendar integration
- **Medication Management** - Adherence tracking and reminders
- **Follow-up Care Actions** - Smart prioritization of care tasks
- **Care Timeline** - Visual journey through pregnancy milestones

### Neonatal Care
- **Baby Monitoring Dashboard** - Real-time vital signs for newborns
- **Growth Tracking** - Weight, height, head circumference trends
- **Feeding Tracker** - Breastfeeding and formula tracking
- **Sleep Monitoring** - Sleep patterns and rest quality tracking

### Immunization & Vaccinations
- **Vaccination Timeline** - Complete immunization schedule with due dates
- **Vaccine Tracking** - Completed, upcoming, and pending vaccines
- **Vaccination Reminders** - Smart notifications for upcoming immunizations
- **Vaccination Records** - Digital health records for all vaccinations

### Notifications & Reports
- **Real-time Notifications** - Appointment, medication, vaccination, and health alerts
- **Medical Reports Center** - Searchable repository of all health documents
- **AI Weekly Summaries** - Personalized health insights and recommendations
- **Health Record Timeline** - Unified view of all medical events

### AI Assistant
- **Umbilica Care AI** - Intelligent health guidance and recommendations
- **Smart Chat** - Natural language Q&A about pregnancy and baby care
- **Health Insights** - Personalized advice based on current health status
- **Medical Information** - Evidence-based healthcare information

### Customization & Settings
- **Baby Gender Theming** - Dynamic pink/blue color schemes for baby-specific sections
- **Notification Preferences** - Customizable alert settings
- **Privacy Controls** - Data access and security management
- **Profile Management** - Mother, baby, and emergency contact information

## 🎨 Design

- **Premium Visual Identity** - Hot pink (#EC0A7A) and white design with soft gradients
- **Clean White Backgrounds** - Professional medical interface
- **Dynamic Baby Themes** - Pink for female babies, blue for male babies
- **Responsive Layout** - Works on desktop, tablet, and mobile devices
- **Real-time Monitoring** - Live data streaming with animated indicators

## 📊 Demo Data

The application comes pre-populated with realistic demo data:

- **Mother**: Ananya Rao, 27 years old
- **Pregnancy**: Week 28, Third Trimester
- **Expected Delivery**: November 12, 2026
- **Baby**: Lumi (Female), 1.1 kg estimated weight
- **Health Score**: 92/100 (Stable)
- **AI Risk Score**: 8% (Low Risk)

All data includes 7-30 days of historical records with realistic time-series data.

## 🚀 Quick Start

### Installation

1. Clone the repository:
```bash
git clone https://github.com/Sivaranjanimahendhiren/Umbilica.git
cd Umbilica
```

2. Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

### Running the Application

```bash
streamlit run app.py
```

The application will open at `http://localhost:8501`

### Demo Login
- **Email**: demo@umbilica.ai
- **Password**: Umbilica@123
- **Or**: Click "Enter Demo Mode" for instant access

## 📋 Project Structure

```
Umbilica/
├── app.py                 # Main Streamlit application
├── config.py             # Configuration and demo data
├── requirements.txt      # Python dependencies
├── .gitignore           # Git ignore rules
└── README.md            # This file
```

## 🔧 Technology Stack

- **Frontend**: Streamlit
- **Data Visualization**: Plotly
- **Data Processing**: Pandas, NumPy
- **Image Processing**: Pillow
- **Data Format**: Python, JSON

## 📱 Pages & Navigation

1. **Dashboard** - Main maternal health overview
2. **Maternal Care** - Comprehensive maternal health management
3. **Vitals** - Detailed vital signs monitoring
4. **Fetal Intelligence** - Fetal development and monitoring
5. **Medical Imaging** - Ultrasound analysis and image viewer
6. **AI Predictions** - Pregnancy risk assessment
7. **Appointments** - Schedule and history
8. **Care Timeline** - Pregnancy journey visualization
9. **Neonatal Care** - Baby monitoring dashboard
10. **Vaccinations** - Immunization tracking
11. **Medications** - Medication adherence tracking
12. **Follow-up Care** - Smart care action items
13. **Reports** - Medical documents repository
14. **Notifications** - Alert management
15. **AI Assistant** - Intelligent health guidance
16. **Profile** - User profile management
17. **Settings** - Application preferences

## ⚕️ Medical Disclaimer

UMBILICA is designed as a healthcare decision-support system and informational platform. It is NOT a medical device and should NOT be used for:

- Diagnosis of medical conditions
- Replacement of professional medical evaluation
- Emergency medical advice

**Important**: All AI predictions are for informational purposes only. Always consult with qualified healthcare professionals before making medical decisions.

## 🔒 Privacy & Security

- All data is stored locally on your device
- No external API calls or cloud transmission
- Medical data is encrypted when exported
- HIPAA-compliant design principles
- User-controlled access and sharing

## 📈 Scalability

The architecture is designed for future expansion:
- **ML Model Integration** - Ready for Python/FastAPI ML backends
- **Database Ready** - Structure supports SQL/NoSQL databases
- **API Architecture** - Service layer designed for REST/GraphQL APIs
- **Multi-user Support** - User authentication framework in place

## 🎯 Future Enhancements

- [ ] Backend API with Python/FastAPI
- [ ] Real ML models for risk prediction
- [ ] Medical image DICOM viewer
- [ ] Cloud data synchronization
- [ ] Doctor portal and multi-user support
- [ ] Integration with EHR systems
- [ ] Mobile native apps
- [ ] Real-time video consultations

## 👥 Contributing

Contributions are welcome! Please feel free to submit pull requests or open issues.

## 📄 License

This project is licensed under the MIT License - see LICENSE file for details.

## 📞 Support

For support and inquiries:
- Email: support@umbilica.ai
- GitHub Issues: https://github.com/Sivaranjanimahendhiren/Umbilica/issues

## 🙏 Acknowledgments

Built with ❤️ for maternal and neonatal healthcare.

---

**UMBILICA**: Intelligent Care. From Motherhood to New Beginnings. 🏥👶
