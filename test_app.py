#!/usr/bin/env python3
"""
Test script for the Cattle Monitoring Platform
"""

import requests
import json
import time
import sys

def test_application():
    """Test the Flask application endpoints"""
    base_url = "http://localhost:5000"
    
    print("🧪 Testing Cattle Monitoring Platform...")
    print("=" * 50)
    
    # Test 1: Check if server is running
    try:
        response = requests.get(base_url, timeout=5)
        print("✅ Server is running")
    except requests.exceptions.RequestException as e:
        print(f"❌ Server is not running: {e}")
        print("Please start the server with: python app.py")
        return False
    
    # Test 2: Test login page
    try:
        response = requests.get(f"{base_url}/login")
        if response.status_code == 200:
            print("✅ Login page loads correctly")
        else:
            print(f"❌ Login page failed: {response.status_code}")
    except Exception as e:
        print(f"❌ Login page error: {e}")
    
    # Test 3: Test milk prediction API
    try:
        milk_data = {
            "feed_kg": 12.0,
            "temp_c": 25.0,
            "humidity": 60,
            "milking_time": 15.0
        }
        
        response = requests.post(
            f"{base_url}/predict_milk",
            json=milk_data,
            headers={"Content-Type": "application/json"}
        )
        
        if response.status_code == 200:
            result = response.json()
            if result.get("success"):
                print(f"✅ Milk prediction API works: {result['predicted_milk']} liters")
            else:
                print(f"❌ Milk prediction failed: {result.get('error')}")
        else:
            print(f"❌ Milk prediction API error: {response.status_code}")
    except Exception as e:
        print(f"❌ Milk prediction error: {e}")
    
    # Test 4: Test disease detection API
    try:
        disease_data = {
            "cow_id": "COW001",
            "day": 15,
            "months_after_birth": 6,
            "previous_mastitis": 0,
            "temperature": 38.5,
            "breed": "Holstein"
        }
        
        response = requests.post(
            f"{base_url}/predict_disease",
            json=disease_data,
            headers={"Content-Type": "application/json"}
        )
        
        if response.status_code == 200:
            result = response.json()
            if result.get("success"):
                print(f"✅ Disease detection API works: {result['risk_level']} risk")
            else:
                print(f"❌ Disease detection failed: {result.get('error')}")
        else:
            print(f"❌ Disease detection API error: {response.status_code}")
    except Exception as e:
        print(f"❌ Disease detection error: {e}")
    
    # Test 5: Test report export
    try:
        response = requests.get(f"{base_url}/export_report?format=csv")
        if response.status_code == 200:
            print("✅ Report export works")
        else:
            print(f"❌ Report export failed: {response.status_code}")
    except Exception as e:
        print(f"❌ Report export error: {e}")
    
    print("=" * 50)
    print("🎉 Testing completed!")
    print("\n📱 To access the application:")
    print("1. Open your browser")
    print("2. Go to http://localhost:5000")
    print("3. Login with: farmer1 / password123")
    print("4. Explore the features!")
    
    return True

if __name__ == "__main__":
    test_application()
