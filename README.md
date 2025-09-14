# Cattle Monitoring Platform

An AI-powered web application for dairy farm management that provides milk yield prediction and disease detection using machine learning models.

## Features

### 🥛 Milk Yield Prediction
- **Accuracy**: 99.4% using Linear Regression
- **Inputs**: Feed quantity, temperature, humidity, milking time
- **Output**: Predicted daily milk yield in liters

### 🏥 Disease Detection
- **Accuracy**: 99.29% ROC AUC using XGBoost
- **Inputs**: Cow ID, health indicators, breed, temperature
- **Output**: Risk assessment and recommendations

### 🌐 Bilingual Support
- English (default)
- Gujarati (ગુજરાતી)

### 📊 Reporting
- Export reports in CSV and PDF formats
- Comprehensive farm analytics
- Historical data tracking

## Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd cattle-monitoring-platform
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   python app.py
   ```

4. **Access the application**
   - Open your browser and go to `http://localhost:5000`
   - Use demo credentials:
     - Username: `farmer1`
     - Password: `password123`

## Usage

### Login
- Use the provided demo credentials to access the platform
- The interface supports both English and Gujarati languages

### Milk Yield Prediction
1. Navigate to "Milk Yield Prediction"
2. Enter the required parameters:
   - Feed quantity (5-25 kg)
   - Temperature (15-40°C)
   - Humidity (30-90%)
   - Milking time (5-30 minutes)
3. Click "Predict Milk Yield" to get the prediction

### Disease Detection
1. Navigate to "Disease Detection"
2. Enter cow information:
   - Cow ID
   - Day of month
   - Months after birth
   - Previous mastitis history
   - Body temperature
   - Breed
3. Click "Predict Disease" to get risk assessment

### Reports
- Click "Export Report" to download comprehensive reports
- Available formats: CSV, PDF
- Includes model performance metrics and recommendations

## Technical Details

### Backend
- **Framework**: Flask (Python)
- **Models**: 
  - Linear Regression for milk prediction
  - XGBoost for disease detection
- **Database**: In-memory (demo purposes)

### Frontend
- **Framework**: Bootstrap 5
- **Icons**: Font Awesome
- **Responsive**: Mobile-friendly design
- **Languages**: English/Gujarati support

### Machine Learning Models

#### Milk Yield Prediction Model
- **Algorithm**: Linear Regression with feature engineering
- **Features**: Feed_kg, Temp_C, Humidity, Milking_Time_min, temp_humidity_ratio
- **Performance**: 99.4% accuracy, 0.994 R² score
- **Preprocessing**: StandardScaler, outlier clipping

#### Disease Detection Model
- **Algorithm**: XGBoost Classifier
- **Features**: 19 health indicators including sensor data
- **Performance**: 99.29% ROC AUC
- **Cross-validation**: GroupKFold to prevent data leakage

## File Structure

```
cattle-monitoring-platform/
├── app.py                 # Flask application
├── requirements.txt       # Python dependencies
├── README.md             # This file
├── templates/            # HTML templates
│   ├── base.html         # Base template
│   ├── login.html        # Login page
│   ├── dashboard.html    # Main dashboard
│   ├── milk_prediction.html
│   └── disease_detection.html
├── static/               # Static files
│   ├── css/
│   │   └── style.css     # Custom styles
│   └── js/
│       └── main.js       # JavaScript functions
└── model files/          # Jupyter notebooks with trained models
    ├── model.ipynb       # Milk yield prediction model
    └── modelv.ipynb      # Disease detection model
```

## API Endpoints

- `GET /` - Redirect to dashboard
- `GET /login` - Login page
- `POST /login` - Process login
- `GET /dashboard` - Main dashboard
- `GET /milk_prediction` - Milk prediction page
- `GET /disease_detection` - Disease detection page
- `POST /predict_milk` - Predict milk yield
- `POST /predict_disease` - Predict disease risk
- `GET /export_report` - Export reports
- `GET /logout` - Logout user

## Model Performance

### Milk Yield Prediction
- **Mean Squared Error**: 0.0317
- **R² Score**: 0.9940
- **Cross-validation R²**: 0.9942
- **MAPE**: 0.71%

### Disease Detection
- **ROC AUC**: 99.29%
- **Cross-validation**: 5-fold GroupKFold
- **Features**: 19 engineered features
- **Model**: XGBoost with hyperparameter tuning

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

This project is developed for hackathon purposes. Please ensure proper licensing for production use.

## Support

For technical support or questions, please contact the development team.

---

**Note**: This is a demo application created for hackathon presentation. For production use, implement proper security measures, database integration, and model deployment best practices.
