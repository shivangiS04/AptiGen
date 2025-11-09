# 🔄 How to Restart Backend (IMPORTANT!)

## The Issue
The backend code has been updated, but **you need to restart the backend server** for changes to take effect!

## Quick Fix

### Option 1: Using the run script
```bash
# Stop the current backend (Ctrl+C in the terminal running it)
# Then restart:
./run.sh  # Mac/Linux
# or
run.bat   # Windows
```

### Option 2: Manual restart
```bash
# 1. Stop the current backend (Ctrl+C)

# 2. Navigate to backend
cd backend

# 3. Activate virtual environment
source venv/bin/activate  # Mac/Linux
# or
venv\Scripts\activate     # Windows

# 4. Start the server
python app.py
```

## Why This Happens
- Python loads modules into memory when the server starts
- Changes to `.py` files don't automatically reload
- You must restart the server to load the new code

## How to Verify It's Working

After restarting, test with different queries:

1. **"Java developer"** → Should show Java assessment first
2. **"Python programmer"** → Should show Python assessment first  
3. **"Leadership teamwork"** → Should show behavioral assessments
4. **"SQL database"** → Should show SQL assessment first

Each query should give **different results** based on relevance!

## Still Having Issues?

If recommendations are still the same:

1. **Check the terminal** - Make sure you restarted the backend
2. **Clear browser cache** - Hard refresh (Ctrl+Shift+R or Cmd+Shift+R)
3. **Check API URL** - Make sure frontend is pointing to the right backend
4. **Check console** - Open browser DevTools and check for errors

## Quick Test

Open a new terminal and run:
```bash
curl -X POST http://localhost:8000/recommend \
  -H "Content-Type: application/json" \
  -d '{"query": "Java developer"}'
```

You should see Java-related assessments at the top!
