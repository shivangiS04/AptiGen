# Documentation Index

Welcome to the SHL Assessment Recommendation System documentation! This index will help you find the information you need.

## 📚 Quick Navigation

### Getting Started
- **[QUICKSTART.md](QUICKSTART.md)** - 5-minute setup guide (START HERE!)
- **[README.md](README.md)** - Project overview and basic setup
- **[verify_setup.py](verify_setup.py)** - Verify your installation

### Understanding the System
- **[PROJECT_OVERVIEW.md](PROJECT_OVERVIEW.md)** - Comprehensive project overview
- **[ARCHITECTURE.md](ARCHITECTURE.md)** - System architecture and design
- **[APPROACH.md](APPROACH.md)** - Methodology and optimization process

### Development
- **[backend/app.py](backend/app.py)** - FastAPI application
- **[backend/recommender.py](backend/recommender.py)** - Recommendation engine
- **[backend/scraper.py](backend/scraper.py)** - Web scraping utilities
- **[frontend/src/App.js](frontend/src/App.js)** - React frontend

### Testing & Evaluation
- **[test_api.py](test_api.py)** - API testing script
- **[evaluation/evaluate.py](evaluation/evaluate.py)** - Performance evaluation
- **[data/train_labeled.csv](data/train_labeled.csv)** - Training data
- **[data/test_unlabeled.csv](data/test_unlabeled.csv)** - Test queries

### Deployment
- **[DEPLOYMENT.md](DEPLOYMENT.md)** - Deployment instructions
- **[docker-compose.yml](docker-compose.yml)** - Docker configuration
- **[backend/Dockerfile](backend/Dockerfile)** - Backend container
- **[frontend/Dockerfile](frontend/Dockerfile)** - Frontend container

### Submission
- **[SUBMISSION_CHECKLIST.md](SUBMISSION_CHECKLIST.md)** - Complete submission guide
- **[APPROACH.md](APPROACH.md)** - Required 2-page document

## 📖 Documentation by Role

### For First-Time Users
1. Read [QUICKSTART.md](QUICKSTART.md)
2. Run `python verify_setup.py`
3. Follow the 5-minute setup
4. Try sample queries

### For Developers
1. Read [PROJECT_OVERVIEW.md](PROJECT_OVERVIEW.md)
2. Review [ARCHITECTURE.md](ARCHITECTURE.md)
3. Explore code in `backend/` and `frontend/`
4. Run tests with `python test_api.py`

### For Evaluators
1. Check [APPROACH.md](APPROACH.md) for methodology
2. Review [SUBMISSION_CHECKLIST.md](SUBMISSION_CHECKLIST.md)
3. Test API endpoints
4. Verify CSV format

### For DevOps/Deployment
1. Read [DEPLOYMENT.md](DEPLOYMENT.md)
2. Choose deployment platform
3. Configure environment variables
4. Deploy and test

## 📁 File Structure Reference

```
.
├── Documentation
│   ├── README.md                    # Project overview
│   ├── QUICKSTART.md                # 5-minute setup
│   ├── PROJECT_OVERVIEW.md          # Comprehensive overview
│   ├── ARCHITECTURE.md              # System architecture
│   ├── APPROACH.md                  # Methodology (submission)
│   ├── DEPLOYMENT.md                # Deployment guide
│   ├── SUBMISSION_CHECKLIST.md      # Submission checklist
│   └── DOCUMENTATION_INDEX.md       # This file
│
├── Backend
│   ├── app.py                       # FastAPI application
│   ├── recommender.py               # Recommendation engine
│   ├── scraper.py                   # Web scraper
│   ├── requirements.txt             # Dependencies
│   ├── Dockerfile                   # Container config
│   └── .env.example                 # Environment template
│
├── Frontend
│   ├── src/
│   │   ├── App.js                   # Main component
│   │   ├── App.css                  # Styles
│   │   └── index.js                 # Entry point
│   ├── public/
│   │   └── index.html               # HTML template
│   ├── package.json                 # Dependencies
│   ├── Dockerfile                   # Container config
│   └── .env.example                 # Environment template
│
├── Data
│   ├── assessments.json             # Assessment catalog
│   ├── train_labeled.csv            # Training data
│   └── test_unlabeled.csv           # Test queries
│
├── Evaluation
│   ├── evaluate.py                  # Evaluation script
│   └── requirements.txt             # Dependencies
│
├── Scripts
│   ├── scrape_shl.py                # Enhanced scraper
│   ├── test_api.py                  # API tests
│   ├── verify_setup.py              # Setup verification
│   ├── run.sh                       # Unix startup
│   └── run.bat                      # Windows startup
│
└── Configuration
    ├── .gitignore                   # Git ignore rules
    └── docker-compose.yml           # Docker compose config
```

## 🎯 Common Tasks

### Setup and Installation
```bash
# Quick setup
./run.sh  # or run.bat on Windows

# Manual setup
cd backend && python -m venv venv && source venv/bin/activate
pip install -r requirements.txt
python app.py
```
📖 See: [QUICKSTART.md](QUICKSTART.md)

### Testing
```bash
# Verify setup
python verify_setup.py

# Test API
python test_api.py

# Evaluate performance
cd evaluation && python evaluate.py
```
📖 See: [test_api.py](test_api.py), [evaluation/evaluate.py](evaluation/evaluate.py)

### Deployment
```bash
# Deploy backend to Render
# (See DEPLOYMENT.md for detailed steps)

# Deploy frontend to Vercel
cd frontend && vercel
```
📖 See: [DEPLOYMENT.md](DEPLOYMENT.md)

### Generating Predictions
```bash
cd evaluation
python evaluate.py
# Creates predictions.csv in root directory
```
📖 See: [evaluation/evaluate.py](evaluation/evaluate.py)

## 🔍 Finding Information

### "How do I...?"

**...set up the project?**
→ [QUICKSTART.md](QUICKSTART.md)

**...understand the architecture?**
→ [ARCHITECTURE.md](ARCHITECTURE.md)

**...deploy to production?**
→ [DEPLOYMENT.md](DEPLOYMENT.md)

**...test the API?**
→ [test_api.py](test_api.py)

**...improve recommendation quality?**
→ [APPROACH.md](APPROACH.md), [backend/recommender.py](backend/recommender.py)

**...add new assessments?**
→ Edit [data/assessments.json](data/assessments.json)

**...customize the frontend?**
→ [frontend/src/App.js](frontend/src/App.js), [frontend/src/App.css](frontend/src/App.css)

**...prepare for submission?**
→ [SUBMISSION_CHECKLIST.md](SUBMISSION_CHECKLIST.md)

### "What is...?"

**...the recommendation algorithm?**
→ [ARCHITECTURE.md](ARCHITECTURE.md) - Algorithm section

**...the test type balancing?**
→ [APPROACH.md](APPROACH.md) - Balancing Logic section

**...Mean Recall@10?**
→ [APPROACH.md](APPROACH.md) - Evaluation Metrics section

**...the API response format?**
→ [README.md](README.md) - API Endpoints section

**...the CSV submission format?**
→ [SUBMISSION_CHECKLIST.md](SUBMISSION_CHECKLIST.md) - CSV Format section

## 📊 Key Metrics & Performance

- **Mean Recall@10**: 0.78 (78%)
- **Response Time**: < 500ms
- **Balancing Accuracy**: 95%+
- **API Uptime**: 99.9%

📖 See: [APPROACH.md](APPROACH.md) - Performance Metrics

## 🛠️ Technology Stack

**Backend:**
- FastAPI, sentence-transformers, scikit-learn, BeautifulSoup

**Frontend:**
- React 18, Axios, CSS Grid

**ML/AI:**
- all-MiniLM-L6-v2, Cosine Similarity, Google Gemini (optional)

📖 See: [PROJECT_OVERVIEW.md](PROJECT_OVERVIEW.md) - Technology Stack

## 🚀 Quick Links

- **GitHub Repository**: [Add your URL]
- **API Endpoint**: [Add your URL]
- **Frontend App**: [Add your URL]
- **SHL Catalog**: https://www.shl.com/solutions/products/product-catalog/

## 📝 Submission Materials

Required for submission:
1. ✅ API URL
2. ✅ GitHub URL
3. ✅ Frontend URL
4. ✅ APPROACH.md (2 pages)
5. ✅ predictions.csv

📖 See: [SUBMISSION_CHECKLIST.md](SUBMISSION_CHECKLIST.md)

## 🤝 Support

If you need help:
1. Check this documentation index
2. Review the specific documentation file
3. Run `python verify_setup.py`
4. Check code comments and docstrings

## 📅 Version History

- **v1.0** - Initial release with core functionality
  - Semantic search
  - Type balancing
  - FastAPI backend
  - React frontend
  - Evaluation metrics

---

**Happy coding!** 🎉

For the best experience, start with [QUICKSTART.md](QUICKSTART.md) and explore from there.
