@echo off
REM SHL Assessment Recommendation System - Quick Start Script (Windows)

echo 🚀 SHL Assessment Recommendation System
echo ========================================
echo.

REM Check if virtual environment exists
if not exist "backend\venv" (
    echo 📦 Creating virtual environment...
    cd backend
    python -m venv venv
    cd ..
)

REM Activate virtual environment
echo 🔧 Activating virtual environment...
call backend\venv\Scripts\activate.bat

REM Install backend dependencies
echo 📥 Installing backend dependencies...
pip install -q -r backend\requirements.txt

REM Check if assessments data exists
if not exist "data\assessments.json" (
    echo 📊 Generating sample assessment data...
    python scripts\scrape_shl.py
)

REM Start backend
echo.
echo ✅ Setup complete!
echo.
echo 🌐 Starting API server...
echo    API will be available at: http://localhost:8000
echo    Health check: http://localhost:8000/health
echo.
echo To start the frontend (in a new terminal):
echo    cd frontend ^&^& npm install ^&^& npm start
echo.
echo To test the API (in a new terminal):
echo    python test_api.py
echo.
echo Press Ctrl+C to stop the server
echo.

cd backend
python app.py
