#!/usr/bin/env python3
"""
Demo script for Smart Dairy Farm Management System
This script demonstrates the ML models and API functionality
"""

import requests
import json
import time

def test_api():
    """Test the API endpoints"""
    base_url = "http://localhost:5000"
    
    print("🐄 Smart Dairy Farm Management System - API Demo")
    print("=" * 60)
    
    # Test milk production prediction
    print("\n🥛 Testing Milk Production Prediction...")
    milk_data = {
        "feed_kg": 12.5,
        "temp_c": 26.0,
        "humidity": 65.0,
        "milking_time": 16.0
    }
    
    try:
        response = requests.post(f"{base_url}/api/predict-milk", json=milk_data)
        if response.status_code == 200:
            result = response.json()
            print(f"✅ Prediction: {result['prediction']} liters")
            print(f"✅ Confidence: {result['confidence']}%")
            print(f"✅ Recommendations: {len(result['recommendations'])} suggestions")
        else:
            print(f"❌ Error: {response.status_code}")
    except Exception as e:
        print(f"❌ Connection error: {e}")
        return
    
    # Test disease detection
    print("\n🏥 Testing Disease Detection...")
    disease_data = {
        "iufl": 200,
        "eufl": 250,
        "iufr": 200,
        "eufr": 250,
        "iurl": 200,
        "eurl": 250,
        "iurr": 200,
        "eurr": 250,
        "temperature": 43.5,
        "hardness": 0,
        "pain": 0,
        "milk_visibility": 0
    }
    
    try:
        response = requests.post(f"{base_url}/api/detect-disease", json=disease_data)
        if response.status_code == 200:
            result = response.json()
            print(f"✅ Status: {result['disease_status']}")
            print(f"✅ Risk Level: {result['risk_level']}")
            print(f"✅ Probability: {result['probability']}%")
        else:
            print(f"❌ Error: {response.status_code}")
    except Exception as e:
        print(f"❌ Connection error: {e}")
    
    # Test farm analytics
    print("\n📊 Testing Farm Analytics...")
    try:
        response = requests.get(f"{base_url}/api/farm-analytics")
        if response.status_code == 200:
            result = response.json()
            print(f"✅ Total Production: {result['total_milk_production']} liters")
            print(f"✅ Daily Average: {result['average_daily_production']} liters")
            print(f"✅ Top Cows: {len(result['top_performing_cows'])} identified")
        else:
            print(f"❌ Error: {response.status_code}")
    except Exception as e:
        print(f"❌ Connection error: {e}")
    
    # Test health alerts
    print("\n🚨 Testing Health Alerts...")
    try:
        response = requests.get(f"{base_url}/api/health-alerts")
        if response.status_code == 200:
            result = response.json()
            print(f"✅ Total Alerts: {result['total_alerts']}")
            if result['alerts']:
                for alert in result['alerts'][:3]:  # Show first 3 alerts
                    print(f"   - {alert['type']}: {alert['message']}")
            else:
                print("   - No alerts (all systems healthy)")
        else:
            print(f"❌ Error: {response.status_code}")
    except Exception as e:
        print(f"❌ Connection error: {e}")
    
    print("\n" + "=" * 60)
    print("🎉 Demo completed! Check the web interface at http://localhost:5000")
    print("💡 Try different input values to see how the predictions change")

if __name__ == "__main__":
    print("⏳ Waiting for server to start...")
    time.sleep(3)  # Wait for server to start
    test_api()
