# Quick Start Guide

## 🚀 Get Started in 5 Minutes

### Step 1: Clone and Setup (2 min)

```bash
# Clone the repository
git clone <your-repo-url>
cd shl-assessment-recommender

# Verify setup
python3 verify_setup.py
```

### Step 2: Start Backend (1 min)

**Option A: Using the run script (Recommended)**
```bash
# Mac/Linuxx
./run.sh
# Windows
run.bat
```

**Option B: Manual setup**
```bash
cd backend
python3 -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

Backend runs at: `http://localhost:8000`

### Step 3: Start Frontend (2 min)

Open a new terminal:

```bash
cd frontend
npm install
npm start
```

Frontend runs at: `http://localhost:3000`

### Step 4: Test It! (30 sec)

**Test the API:**
```bash
python test_api.py
```

**Try the web interface:**
1. Open `http://localhost:3000`
2. Enter a query: "Java developer with teamwork skills"
3. Click "Get Recommendations"
4. See 5-10 balanced recommendations!

## 📊 Generate Predictions

```bash
cd evaluation
python evaluate.py
```

This creates `predictions.csv` in the root directory.

## 🧪 Sample Queries to Try

1. "I am hiring for Java developers who can also collaborate effectively with my business teams."
2. "Looking to hire mid-level professionals who are proficient in Python, SQL and JavaScript."
3. "Need assessments for an analyst role with cognitive and personality tests."
4. "Senior software engineer with strong problem-solving skills"
5. "Marketing specialist with creative and analytical capabilities"

## 🔍 What to Expect

**Query:** "Java developer with teamwork skills"

**Response:** 5-10 assessments including:
- Java Programming Assessment (Type: K)
- Teamwork and Collaboration Assessment (Type: P)
- Technology Professional Assessment (Type: P)
- Cognitive Ability Test (Type: A)
- And more...

Notice the **balance** between:
- **K** (Knowledge & Skills) - Technical assessments
- **P** (Personality & Behavior) - Soft skills
- **A** (Ability & Aptitude) - Cognitive tests

## 📁 Project Structure

```
.
├── backend/           # FastAPI backend
│   ├── app.py        # Main API
│   ├── recommender.py # Recommendation engine
│   └── scraper.py    # Web scraper
├── frontend/         # React frontend
│   └── src/
│       ├── App.js    # Main component
│       └── App.css   # Styles
├── data/            # Assessment data
│   ├── assessments.json
│   ├── train_labeled.csv
│   └── test_unlabeled.csv
├── evaluation/      # Evaluation scripts
│   └── evaluate.py
└── scripts/         # Utility scripts
    └── scrape_shl.py
```

## 🐛 Troubleshooting

**Issue:** "Module not found"
```bash
# Make sure you're in the virtual environment
source backend/venv/bin/activate
pip install -r backend/requirements.txt
```

**Issue:** "Port already in use"
```bash
# Kill the process using port 8000
lsof -ti:8000 | xargs kill -9  # Mac/Linux
# Or change port in app.py: uvicorn.run(app, port=8001)
```

**Issue:** "CORS error in frontend"
```bash
# Make sure backend is running first
# Check REACT_APP_API_URL in frontend/.env
```

**Issue:** "No assessments found"
```bash
# Generate sample data
python scripts/scrape_shl.py
```

