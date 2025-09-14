#!/usr/bin/env python3
"""
Train and save ML models for the Smart Dairy Farm Management System
"""

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor, RandomForestClassifier
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.metrics import r2_score, accuracy_score, classification_report
import pickle
import os

def train_milk_production_model():
    """Train the milk production prediction model"""
    print("🥛 Training Milk Production Model...")
    
    # Load data
    df = pd.read_csv('farm_milk_production.csv')
    
    # Feature engineering (matching the notebook)
    df['temp_humidity_ratio'] = df['Temp_C'] / (df['Humidity'] + 1)
    
    # Prepare features
    X = df[['Feed_kg', 'Milking_Time_min', 'temp_humidity_ratio']].copy()
    y = df['Milk_Liters']
    
    # Handle outliers
    for col in X.columns:
        q1 = X[col].quantile(0.25)
        q3 = X[col].quantile(0.75)
        iqr = q3 - q1
        X[col] = X[col].clip(q1 - 1.5*iqr, q3 + 1.5*iqr)
    
    # Split data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Create pipeline
    pipeline = Pipeline([
        ('scaler', StandardScaler()),
        ('model', RandomForestRegressor(n_estimators=100, random_state=42))
    ])
    
    # Train model
    pipeline.fit(X_train, y_train)
    
    # Evaluate
    y_pred = pipeline.predict(X_test)
    r2 = r2_score(y_test, y_pred)
    print(f"✅ Milk Production Model R² Score: {r2:.4f}")
    
    # Save model
    with open('milk_production_model.pkl', 'wb') as f:
        pickle.dump(pipeline, f)
    print("✅ Milk production model saved successfully")
    
    return pipeline

def train_disease_detection_model():
    """Train the disease detection model"""
    print("🏥 Training Disease Detection Model...")
    
    # Load data
    df = pd.read_csv('clinical_mastitis_cows_version1.csv')
    
    # Prepare features
    feature_cols = ['IUFL', 'EUFL', 'IUFR', 'EUFR', 'IURL', 'EURL', 'IURR', 'EURR', 
                   'Temperature', 'Hardness', 'Pain', 'Milk_visibility']
    X = df[feature_cols].copy()
    y = df['class1']  # 0 = healthy, 1 = mastitis
    
    # Split data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Create pipeline
    pipeline = Pipeline([
        ('scaler', StandardScaler()),
        ('model', RandomForestClassifier(n_estimators=100, random_state=42))
    ])
    
    # Train model
    pipeline.fit(X_train, y_train)
    
    # Evaluate
    y_pred = pipeline.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print(f"✅ Disease Detection Model Accuracy: {accuracy:.4f}")
    
    # Save model
    with open('cattle_disease_detector.pkl', 'wb') as f:
        pickle.dump(pipeline, f)
    print("✅ Disease detection model saved successfully")
    
    return pipeline

def create_ensemble_model():
    """Create an ensemble model combining both predictions"""
    print("🤖 Creating Ensemble Model...")
    
    # Load individual models
    with open('milk_production_model.pkl', 'rb') as f:
        milk_model = pickle.load(f)
    
    with open('cattle_disease_detector.pkl', 'rb') as f:
        disease_model = pickle.load(f)
    
    # Create ensemble
    ensemble = {
        'milk_model': milk_model,
        'disease_model': disease_model,
        'version': '1.0',
        'trained_date': pd.Timestamp.now().strftime('%Y-%m-%d %H:%M:%S')
    }
    
    # Save ensemble
    with open('complete_detector.pkl', 'wb') as f:
        pickle.dump(ensemble, f)
    print("✅ Ensemble model saved successfully")
    
    return ensemble

def main():
    """Main training function"""
    print("🚀 Starting ML Model Training...")
    print("=" * 50)
    
    try:
        # Train models
        milk_model = train_milk_production_model()
        disease_model = train_disease_detection_model()
        ensemble = create_ensemble_model()
        
        print("\n" + "=" * 50)
        print("🎉 All models trained and saved successfully!")
        print("📁 Files created:")
        print("   - milk_production_model.pkl")
        print("   - cattle_disease_detector.pkl") 
        print("   - complete_detector.pkl")
        print("\n🔄 Restart the Flask app to use the trained models")
        
    except Exception as e:
        print(f"❌ Error during training: {e}")
        return False
    
    return True

if __name__ == "__main__":
    main()
