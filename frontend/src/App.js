import React, { useState } from 'react';
import axios from 'axios';
import './App.css';

const API_URL = process.env.REACT_APP_API_URL || 'http://localhost:8000';

function App() {
  const [query, setQuery] = useState('');
  const [recommendations, setRecommendations] = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    
    if (!query.trim()) {
      setError('Please enter a query');
      return;
    }

    setLoading(true);
    setError('');
    setRecommendations([]);

    try {
      const response = await axios.post(`${API_URL}/recommend`, {
        query: query
      });

      setRecommendations(response.data.recommended_assessments);
    } catch (err) {
      setError(err.response?.data?.detail || 'Failed to get recommendations');
    } finally {
      setLoading(false);
    }
  };

  const sampleQueries = [
    'I am hiring for Java developers who can also collaborate effectively with my business teams.',
    'Looking to hire mid-level professionals who are proficient in Python, SQL and JavaScript.',
    'Need assessments for an analyst role. Want to screen using Cognitive and personality tests.'
  ];

  return (
    <div className="App">
      <header className="App-header">
        <h1>SHL Assessment Recommendation System</h1>
        <p>Find the right assessments for your hiring needs</p>
      </header>

      <main className="App-main">
        <form onSubmit={handleSubmit} className="query-form">
          <textarea
            value={query}
            onChange={(e) => setQuery(e.target.value)}
            placeholder="Enter your job description or query..."
            rows="4"
            className="query-input"
          />
          <button type="submit" disabled={loading} className="submit-btn">
            {loading ? 'Getting Recommendations...' : 'Get Recommendations'}
          </button>
        </form>

        <div className="sample-queries">
          <h3>Sample Queries:</h3>
          {sampleQueries.map((sq, idx) => (
            <button
              key={idx}
              onClick={() => setQuery(sq)}
              className="sample-query-btn"
            >
              {sq}
            </button>
          ))}
        </div>

        {error && <div className="error">{error}</div>}

        {recommendations.length > 0 && (
          <div className="recommendations">
            <h2>Recommended Assessments ({recommendations.length})</h2>
            <div className="assessment-grid">
              {recommendations.map((assessment, idx) => (
                <div key={idx} className="assessment-card">
                  <div className="assessment-header">
                    <h3>{assessment.name}</h3>
                    <span className="test-type-badge">
                      {assessment.test_type.join(', ')}
                    </span>
                  </div>
                  <p className="assessment-description">{assessment.description}</p>
                  <div className="assessment-details">
                    {assessment.duration && (
                      <span>⏱️ {assessment.duration} min</span>
                    )}
                    <span>🏠 Remote: {assessment.remote_support}</span>
                    <span>📱 Adaptive: {assessment.adaptive_support}</span>
                  </div>
                  <a
                    href={assessment.url}
                    target="_blank"
                    rel="noopener noreferrer"
                    className="view-assessment-btn"
                  >
                    View Assessment →
                  </a>
                </div>
              ))}
            </div>
          </div>
        )}
      </main>

      <footer className="App-footer">
        <div className="footer-content">
          <div className="footer-main">
            <h3 className="pixel-title">⚡ SHL Assessment Recommender AI ⚡</h3>
            <p className="footer-tagline">Intelligent hiring decisions powered by AI</p>
          </div>
          <div className="footer-tech">
            <span className="tech-badge">React</span>
            <span className="tech-badge">FastAPI</span>
            <span className="tech-badge">ML</span>
          </div>
          <div className="footer-credits">
            <p className="made-by">Made with ❤️ by <strong>Shivangi Singh</strong></p>
            <p className="copyright">© 2025 | GenAI Assessment System</p>
          </div>
        </div>
      </footer>
    </div>
  );
}

export default App;
