#!/bin/bash

# SHL Assessment Recommendation System - Quick Start Script

echo "🚀 SHL Assessment Recommendation System"
echo "========================================"
echo ""

# Check if virtual environment exists
if [ ! -d "backend/venv" ]; then
    echo "📦 Creating virtual environment..."
    cd backend
    python3 -m venv venv
    cd ..
fi

# Activate virtual environment
echo "🔧 Activating virtual environment..."
source backend/venv/bin/activate

# Install backend dependencies
echo "📥 Installing backend dependencies..."
pip install -q -r backend/requirements.txt

# Check if assessments data exists
if [ ! -f "data/assessments.json" ]; then
    echo "📊 Generating sample assessment data..."
    python scripts/scrape_shl.py
fi

# Start backend
echo ""
echo "✅ Setup complete!"
echo ""
echo "🌐 Starting API server..."
echo "   API will be available at: http://localhost:8000"
echo "   Health check: http://localhost:8000/health"
echo ""
echo "To start the frontend (in a new terminal):"
echo "   cd frontend && npm install && npm start"
echo ""
echo "To test the API (in a new terminal):"
echo "   python test_api.py"
echo ""
echo "Press Ctrl+C to stop the server"
echo ""

cd backend
python app.py
