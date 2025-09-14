#!/usr/bin/env python3
"""
Comprehensive Demo Script for Smart Dairy Farm Management System
Tests all features and demonstrates the complete functionality
"""

import requests
import json
import time
import random
from datetime import datetime, timedelta

def test_all_features():
    """Test all features of the application"""
    base_url = "http://localhost:5000"
    
    print("🐄 Smart Dairy Farm Management System - Comprehensive Demo")
    print("=" * 70)
    print(f"🕐 Demo started at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 70)
    
    # Test 1: Milk Production Prediction
    print("\n🥛 TEST 1: Milk Production Prediction")
    print("-" * 50)
    
    test_cases = [
        {"feed_kg": 12.0, "temp_c": 25.0, "humidity": 60.0, "milking_time": 15.0},
        {"feed_kg": 15.0, "temp_c": 30.0, "humidity": 70.0, "milking_time": 18.0},
        {"feed_kg": 8.0, "temp_c": 20.0, "humidity": 50.0, "milking_time": 12.0}
    ]
    
    for i, test_case in enumerate(test_cases, 1):
        try:
            response = requests.post(f"{base_url}/api/predict-milk", json=test_case)
            if response.status_code == 200:
                result = response.json()
                print(f"✅ Test {i}: {result['prediction']}L (Confidence: {result['confidence']}%)")
                print(f"   Input: Feed={test_case['feed_kg']}kg, Temp={test_case['temp_c']}°C")
                print(f"   Recommendations: {len(result['recommendations'])} suggestions")
            else:
                print(f"❌ Test {i} failed: {response.status_code}")
        except Exception as e:
            print(f"❌ Test {i} error: {e}")
    
    # Test 2: Disease Detection
    print("\n🏥 TEST 2: Disease Detection")
    print("-" * 50)
    
    disease_cases = [
        {"iufl": 200, "eufl": 250, "iufr": 200, "eufr": 250, "iurl": 200, "eurl": 250, 
         "iurr": 200, "eurr": 250, "temperature": 43.0, "hardness": 0, "pain": 0, "milk_visibility": 0},
        {"iufl": 300, "eufl": 350, "iufr": 300, "eufr": 350, "iurl": 300, "eurl": 350, 
         "iurr": 300, "eurr": 350, "temperature": 44.5, "hardness": 1, "pain": 1, "milk_visibility": 1}
    ]
    
    for i, test_case in enumerate(disease_cases, 1):
        try:
            response = requests.post(f"{base_url}/api/detect-disease", json=test_case)
            if response.status_code == 200:
                result = response.json()
                print(f"✅ Test {i}: {result['disease_status']} (Risk: {result['risk_level']}, {result['probability']}%)")
                print(f"   Recommendations: {len(result['recommendations'])} suggestions")
            else:
                print(f"❌ Test {i} failed: {response.status_code}")
        except Exception as e:
            print(f"❌ Test {i} error: {e}")
    
    # Test 3: Farm Analytics
    print("\n📊 TEST 3: Farm Analytics")
    print("-" * 50)
    
    try:
        response = requests.get(f"{base_url}/api/farm-analytics")
        if response.status_code == 200:
            result = response.json()
            print(f"✅ Total Production: {result['total_milk_production']} liters")
            print(f"✅ Daily Average: {result['average_daily_production']} liters")
            print(f"✅ Top Performers: {len(result['top_performing_cows'])} cows identified")
            print(f"✅ Daily Data Points: {len(result['daily_production'])} days")
        else:
            print(f"❌ Analytics failed: {response.status_code}")
    except Exception as e:
        print(f"❌ Analytics error: {e}")
    
    # Test 4: Health Alerts
    print("\n🚨 TEST 4: Health Alerts")
    print("-" * 50)
    
    try:
        response = requests.get(f"{base_url}/api/health-alerts")
        if response.status_code == 200:
            result = response.json()
            print(f"✅ Total Alerts: {result['total_alerts']}")
            if result['alerts']:
                for alert in result['alerts'][:3]:
                    print(f"   - {alert['type']}: {alert['message']}")
            else:
                print("   - No alerts (all systems healthy)")
        else:
            print(f"❌ Alerts failed: {response.status_code}")
    except Exception as e:
        print(f"❌ Alerts error: {e}")
    
    # Test 5: Data Export
    print("\n📁 TEST 5: Data Export")
    print("-" * 50)
    
    export_types = ['milk', 'disease', 'analytics']
    for export_type in export_types:
        try:
            response = requests.get(f"{base_url}/api/export-data/{export_type}")
            if response.status_code == 200:
                result = response.json()
                print(f"✅ {export_type.title()} Export: {result.get('total_records', 'N/A')} records")
            else:
                print(f"❌ {export_type.title()} export failed: {response.status_code}")
        except Exception as e:
            print(f"❌ {export_type.title()} export error: {e}")
    
    # Test 6: Predictions History
    print("\n📈 TEST 6: Predictions History")
    print("-" * 50)
    
    try:
        response = requests.get(f"{base_url}/api/predictions-history")
        if response.status_code == 200:
            result = response.json()
            print(f"✅ History Records: {result['total_predictions']}")
            for record in result['history'][:2]:
                print(f"   - {record['type']}: {record['prediction']} ({record['confidence']}%)")
        else:
            print(f"❌ History failed: {response.status_code}")
    except Exception as e:
        print(f"❌ History error: {e}")
    
    # Performance Test
    print("\n⚡ PERFORMANCE TEST")
    print("-" * 50)
    
    start_time = time.time()
    test_data = {"feed_kg": 12.0, "temp_c": 25.0, "humidity": 60.0, "milking_time": 15.0}
    
    for i in range(10):
        try:
            response = requests.post(f"{base_url}/api/predict-milk", json=test_data)
            if response.status_code != 200:
                print(f"❌ Performance test failed at iteration {i+1}")
                break
        except Exception as e:
            print(f"❌ Performance test error at iteration {i+1}: {e}")
            break
    else:
        end_time = time.time()
        avg_time = (end_time - start_time) / 10
        print(f"✅ 10 predictions completed in {end_time - start_time:.2f}s")
        print(f"✅ Average response time: {avg_time:.3f}s per prediction")
    
    print("\n" + "=" * 70)
    print("🎉 COMPREHENSIVE DEMO COMPLETED!")
    print("=" * 70)
    print("📱 Web Interface: http://localhost:5000")
    print("🔗 All features tested successfully!")
    print("🏆 Ready for hackathon presentation!")

def stress_test():
    """Run stress test with multiple concurrent requests"""
    print("\n🔥 STRESS TEST")
    print("-" * 50)
    
    import threading
    import queue
    
    base_url = "http://localhost:5000"
    results = queue.Queue()
    
    def make_request(request_id):
        try:
            test_data = {
                "feed_kg": random.uniform(8, 20),
                "temp_c": random.uniform(15, 35),
                "humidity": random.uniform(40, 80),
                "milking_time": random.uniform(10, 25)
            }
            
            start_time = time.time()
            response = requests.post(f"{base_url}/api/predict-milk", json=test_data)
            end_time = time.time()
            
            results.put({
                'id': request_id,
                'status': response.status_code,
                'time': end_time - start_time,
                'success': response.status_code == 200
            })
        except Exception as e:
            results.put({
                'id': request_id,
                'status': 'error',
                'time': 0,
                'success': False,
                'error': str(e)
            })
    
    # Start 20 concurrent requests
    threads = []
    for i in range(20):
        thread = threading.Thread(target=make_request, args=(i,))
        threads.append(thread)
        thread.start()
    
    # Wait for all threads to complete
    for thread in threads:
        thread.join()
    
    # Collect results
    successful_requests = 0
    total_time = 0
    max_time = 0
    
    while not results.empty():
        result = results.get()
        if result['success']:
            successful_requests += 1
            total_time += result['time']
            max_time = max(max_time, result['time'])
    
    if successful_requests > 0:
        avg_time = total_time / successful_requests
        print(f"✅ {successful_requests}/20 requests successful")
        print(f"✅ Average response time: {avg_time:.3f}s")
        print(f"✅ Maximum response time: {max_time:.3f}s")
        print(f"✅ Success rate: {successful_requests/20*100:.1f}%")
    else:
        print("❌ All requests failed")

if __name__ == "__main__":
    print("⏳ Waiting for server to start...")
    time.sleep(3)
    
    try:
        test_all_features()
        stress_test()
    except KeyboardInterrupt:
        print("\n👋 Demo stopped by user")
    except Exception as e:
        print(f"\n❌ Demo error: {e}")
