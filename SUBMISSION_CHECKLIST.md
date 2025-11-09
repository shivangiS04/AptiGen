# Submission Checklist

## Before Submitting

### 1. Code Repository ✓
- [ ] Push all code to GitHub
- [ ] Make repository public or share with evaluators
- [ ] Ensure README.md is complete
- [ ] Include all necessary files (.gitignore, requirements.txt, etc.)

### 2. API Deployment
- [ ] Deploy backend to cloud platform (Render/Railway/Heroku)
- [ ] Test `/health` endpoint
- [ ] Test `/recommend` endpoint with sample queries
- [ ] Verify response format matches specification
- [ ] Ensure API returns 5-10 recommendations
- [ ] Check that all required fields are present

**API URL to submit:** `_______________________________`

### 3. Frontend Deployment
- [ ] Deploy frontend to Vercel/Netlify/Render
- [ ] Update `REACT_APP_API_URL` environment variable
- [ ] Test the web interface
- [ ] Verify all features work (query input, recommendations display)
- [ ] Test on mobile/responsive view

**Frontend URL to submit:** `_______________________________`

### 4. Generate Predictions CSV
```bash
cd evaluation
python evaluate.py
```

- [ ] Run evaluation script on test set
- [ ] Verify `predictions.csv` is generated in root directory
- [ ] Check CSV format: two columns (Query, Assessment_url)
- [ ] Ensure each query has 5-10 recommendations
- [ ] Verify URLs are valid SHL catalog URLs

**CSV file location:** `predictions.csv`

### 5. Approach Document
- [ ] Complete APPROACH.md (max 2 pages)
- [ ] Include methodology section
- [ ] Document data pipeline
- [ ] Explain technology stack
- [ ] Show evaluation metrics and optimization process
- [ ] Include initial results and improvements
- [ ] Keep it concise with appropriate information

### 6. Testing

**Local Testing:**
```bash
# Verify setup
python verify_setup.py

# Test API
python test_api.py

# Test evaluation
cd evaluation && python evaluate.py
```

**Deployment Testing:**
```bash
# Test health endpoint
curl https://your-api-url.com/health

# Test recommend endpoint
curl -X POST https://your-api-url.com/recommend \
  -H "Content-Type: application/json" \
  -d '{"query": "Java developer with teamwork skills"}'
```

- [ ] All local tests pass
- [ ] Deployed API responds correctly
- [ ] Frontend connects to API successfully
- [ ] CSV generation works

### 7. Final Submission

Submit via the provided form:

**3 URLs:**
1. [ ] API endpoint URL: `_______________________________`
2. [ ] GitHub repository URL: `_______________________________`
3. [ ] Frontend web app URL: `_______________________________`

**2 Files:**
1. [ ] APPROACH.md (2-page document)
2. [ ] predictions.csv (test set predictions)

### 8. Quality Checks

**API Response Format:**
```json
{
  "recommended_assessments": [
    {
      "url": "string",
      "name": "string",
      "adaptive_support": "Yes/No",
      "description": "string",
      "duration": integer,
      "remote_support": "Yes/No",
      "test_type": ["K", "P"]
    }
  ]
}
```

- [ ] Response has `recommended_assessments` array
- [ ] Each assessment has all required fields
- [ ] `test_type` is an array of strings
- [ ] URLs are valid and accessible
- [ ] Returns 5-10 recommendations (not less, not more)

**CSV Format:**
```
Query,Assessment_url
Query 1,Recommendation 1 (URL)
Query 1,Recommendation 2 (URL)
Query 1,Recommendation 3 (URL)
...
Query 2,Recommendation 1
```

- [ ] Exactly 2 columns: Query, Assessment_url
- [ ] Each query has multiple rows (one per recommendation)
- [ ] No extra columns or formatting
- [ ] URLs are complete and valid

### 9. Performance Verification

- [ ] Mean Recall@10 calculated on train set
- [ ] Recommendations are balanced (K, P, A types)
- [ ] API response time < 1 second
- [ ] No errors in logs

### 10. Documentation Review

- [ ] README.md has setup instructions
- [ ] APPROACH.md explains methodology
- [ ] DEPLOYMENT.md has deployment guide
- [ ] Code has comments where needed
- [ ] All scripts are executable

## Common Issues to Avoid

❌ **Don't:**
- Submit API that returns < 5 or > 10 recommendations
- Use wrong CSV format (will fail automated evaluation)
- Include pre-packaged job solutions (only individual tests)
- Forget to test deployed API before submitting
- Submit private GitHub repo without sharing access

✅ **Do:**
- Test all endpoints thoroughly
- Verify CSV format exactly matches specification
- Ensure balanced recommendations for multi-domain queries
- Document your optimization process
- Keep approach document concise (2 pages max)

## Submission Form Fields

When filling the submission form, have ready:

1. **API Endpoint URL**: Full URL including https://
2. **GitHub URL**: Repository URL (public or shared)
3. **Frontend URL**: Deployed web application URL
4. **Approach Document**: Upload APPROACH.md
5. **Predictions CSV**: Upload predictions.csv

## Final Checklist

- [ ] All URLs are accessible and working
- [ ] GitHub repository is public or shared
- [ ] predictions.csv is in correct format
- [ ] APPROACH.md is complete and concise
- [ ] API returns correct response format
- [ ] Frontend displays recommendations properly
- [ ] All tests pass

**Ready to submit!** 🚀
