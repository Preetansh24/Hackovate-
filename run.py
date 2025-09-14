#!/usr/bin/env python3
"""
Smart Dairy Farm Management System
Startup script for the application
"""

import os
import sys
import subprocess
import webbrowser
import time
from threading import Timer

def check_requirements():
    """Check if all required packages are installed"""
    try:
        import flask
        import pandas
        import numpy
        import sklearn
        print("✅ All required packages are installed")
        return True
    except ImportError as e:
        print(f"❌ Missing package: {e}")
        print("Please run: pip install -r requirements.txt")
        return False

def open_browser():
    """Open the application in the default browser"""
    webbrowser.open('http://localhost:5000')

def main():
    """Main startup function"""
    print("🐄 Smart Dairy Farm Management System")
    print("=" * 50)
    
    # Check requirements
    if not check_requirements():
        sys.exit(1)
    
    # Check if data files exist
    data_files = [
        'farm_milk_production.csv',
        'clinical_mastitis_cows_version1.csv'
    ]
    
    missing_files = [f for f in data_files if not os.path.exists(f)]
    if missing_files:
        print(f"⚠️  Warning: Missing data files: {', '.join(missing_files)}")
        print("The application will work with fallback data")
    
    print("\n🚀 Starting the application...")
    print("📱 The application will open in your browser automatically")
    print("🔗 Manual access: http://localhost:5000")
    print("⏹️  Press Ctrl+C to stop the server")
    print("=" * 50)
    
    # Open browser after 2 seconds
    Timer(2.0, open_browser).start()
    
    # Start the Flask application
    try:
        from app import app
        app.run(debug=True, host='0.0.0.0', port=5000)
    except KeyboardInterrupt:
        print("\n👋 Application stopped by user")
    except Exception as e:
        print(f"❌ Error starting application: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
