#!/bin/bash

echo "Starting Cattle Monitoring Platform..."
echo ""
echo "Installing required packages..."
pip install -r requirements.txt
echo ""
echo "Starting the application..."
echo ""
echo "The application will be available at: http://localhost:5000"
echo "Login credentials: farmer1 / password123"
echo ""
echo "Press Ctrl+C to stop the server"
echo ""
python app.py
