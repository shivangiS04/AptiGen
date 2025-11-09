# Deployment Guide

## Local Development

### Backend Setup

```bash
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt

# Optional: Add Gemini API key
cp .env.example .env
# Edit .env and add your GEMINI_API_KEY

# Run the API
python app.py
```

API will be available at `http://localhost:8000`

### Frontend Setup

```bash
cd frontend
npm install
npm start
```

Frontend will be available at `http://localhost:3000`

### Test the API

```bash
# In a new terminal
python test_api.py
```

### Generate Predictions

```bash
cd evaluation
python evaluate.py
```

This will create `predictions.csv` in the root directory.

## Cloud Deployment

### Option 1: Render (Recommended)

**Backend:**
1. Push code to GitHub
2. Go to render.com → New Web Service
3. Connect your repository
4. Configure:
   - Build Command: `cd backend && pip install -r requirements.txt`
   - Start Command: `cd backend && uvicorn app:app --host 0.0.0.0 --port $PORT`
   - Environment: Python 3
5. Add environment variable: `GEMINI_API_KEY` (optional)
6. Deploy

**Frontend:**
1. Render → New Static Site
2. Configure:
   - Build Command: `cd frontend && npm install && npm run build`
   - Publish Directory: `frontend/build`
3. Add environment variable: `REACT_APP_API_URL=<your-backend-url>`
4. Deploy

### Option 2: Railway

**Backend:**
```bash
# Install Railway CLI
npm install -g @railway/cli

# Login and deploy
railway login
cd backend
railway init
railway up
```

**Frontend:**
Deploy to Vercel:
```bash
cd frontend
npm install -g vercel
vercel
```

### Option 3: Heroku

**Backend:**
Create `Procfile` in backend/:
```
web: uvicorn app:app --host 0.0.0.0 --port $PORT
```

Deploy:
```bash
heroku create shl-recommender-api
git subtree push --prefix backend heroku main
```

## Environment Variables

### Backend
- `GEMINI_API_KEY`: (Optional) Google Gemini API key for enhanced recommendations

### Frontend
- `REACT_APP_API_URL`: Backend API URL (e.g., https://your-api.render.com)

## Testing Deployed API

```bash
# Test health endpoint
curl https://your-api-url.com/health

# Test recommend endpoint
curl -X POST https://your-api-url.com/recommend \
  -H "Content-Type: application/json" \
  -d '{"query": "Java developer with teamwork skills"}'
```

## Monitoring

- Check API logs in your deployment platform
- Monitor response times and error rates
- Set up uptime monitoring (e.g., UptimeRobot)

## Troubleshooting

**Issue**: Module not found errors
- Solution: Ensure all dependencies in requirements.txt are installed

**Issue**: CORS errors in frontend
- Solution: Check CORS middleware configuration in app.py

**Issue**: Slow response times
- Solution: Consider caching embeddings or using a vector database

**Issue**: Out of memory
- Solution: Reduce embedding model size or use cloud-based vector search
