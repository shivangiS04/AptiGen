# System Architecture

## High-Level Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                         User Interface                          │
│                      (React Frontend)                           │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐        │
│  │ Query Input  │  │ Sample       │  │ Results      │        │
│  │ Text Area    │  │ Queries      │  │ Display      │        │
│  └──────────────┘  └──────────────┘  └──────────────┘        │
└────────────────────────────┬────────────────────────────────────┘
                             │ HTTP POST /recommend
                             │ {"query": "..."}
                             ▼
┌─────────────────────────────────────────────────────────────────┐
│                      API Layer (FastAPI)                        │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐        │
│  │ /health      │  │ /recommend   │  │ CORS         │        │
│  │ endpoint     │  │ endpoint     │  │ Middleware   │        │
│  └──────────────┘  └──────────────┘  └──────────────┘        │
└────────────────────────────┬────────────────────────────────────┘
                             │
                             ▼
┌─────────────────────────────────────────────────────────────────┐
│                  Recommendation Engine                          │
│                                                                 │
│  ┌─────────────────────────────────────────────────────────┐  │
│  │ 1. Query Analysis                                       │  │
│  │    - Extract technical skills (Java, Python, SQL)      │  │
│  │    - Extract behavioral traits (teamwork, leadership)  │  │
│  │    - Identify required test types (K, P, A, C)        │  │
│  └─────────────────────────────────────────────────────────┘  │
│                             │                                   │
│                             ▼                                   │
│  ┌─────────────────────────────────────────────────────────┐  │
│  │ 2. Embedding Generation                                 │  │
│  │    - Convert query to 384-dim vector                   │  │
│  │    - Use sentence-transformers (all-MiniLM-L6-v2)     │  │
│  └─────────────────────────────────────────────────────────┘  │
│                             │                                   │
│                             ▼                                   │
│  ┌─────────────────────────────────────────────────────────┐  │
│  │ 3. Similarity Search                                    │  │
│  │    - Compute cosine similarity with all assessments    │  │
│  │    - Get top 30 candidates                             │  │
│  └─────────────────────────────────────────────────────────┘  │
│                             │                                   │
│                             ▼                                   │
│  ┌─────────────────────────────────────────────────────────┐  │
│  │ 4. Type Balancing                                       │  │
│  │    - Allocate slots per test type                      │  │
│  │    - Ensure balanced distribution                      │  │
│  │    - Select top 10 recommendations                     │  │
│  └─────────────────────────────────────────────────────────┘  │
└────────────────────────────┬────────────────────────────────────┘
                             │
                             ▼
┌─────────────────────────────────────────────────────────────────┐
│                      Data Layer                                 │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐        │
│  │ assessments  │  │ Pre-computed │  │ Training     │        │
│  │ .json        │  │ Embeddings   │  │ Data CSV     │        │
│  └──────────────┘  └──────────────┘  └──────────────┘        │
└─────────────────────────────────────────────────────────────────┘
```

## Component Details

### 1. Frontend (React)

**Responsibilities:**
- User input collection
- API communication
- Results visualization
- Responsive design

**Key Files:**
- `App.js`: Main component with state management
- `App.css`: Styling and layout
- `index.js`: Entry point

**Flow:**
```
User Input → Validation → API Call → Display Results
```

### 2. API Layer (FastAPI)

**Responsibilities:**
- Request validation
- Error handling
- Response formatting
- CORS management

**Endpoints:**

```python
GET /health
→ Returns: {"status": "healthy"}

POST /recommend
→ Input: {"query": "string"}
→ Output: {
    "recommended_assessments": [
      {
        "url": "string",
        "name": "string",
        "adaptive_support": "Yes/No",
        "description": "string",
        "duration": int,
        "remote_support": "Yes/No",
        "test_type": ["K", "P"]
      }
    ]
  }
```

### 3. Recommendation Engine

**Core Algorithm:**

```
Input: Natural language query
Output: 5-10 balanced assessment recommendations

Steps:
1. Query Analysis
   ├─ Keyword extraction
   ├─ Skill identification
   └─ Test type detection

2. Embedding Generation
   ├─ Tokenization
   ├─ Model inference
   └─ Vector representation

3. Similarity Search
   ├─ Cosine similarity computation
   ├─ Ranking by score
   └─ Top-K selection

4. Type Balancing
   ├─ Proportional allocation
   ├─ Diversity enforcement
   └─ Final selection

5. Response Formatting
   └─ JSON serialization
```

**Balancing Logic:**

```
Example Query: "Java developer with teamwork skills"

Detected Requirements:
├─ Technical: ["java", "programming"]  → Test Type K
└─ Behavioral: ["teamwork"]            → Test Type P

Allocation:
├─ K-type: 5 slots (50%)
└─ P-type: 5 slots (50%)

Selection Process:
1. Sort candidates by similarity score
2. Fill K-type slots (top 5 K-type assessments)
3. Fill P-type slots (top 5 P-type assessments)
4. Return combined list (10 total)
```

### 4. Data Layer

**Assessment Data Structure:**

```json
{
  "name": "Python (New)",
  "url": "https://www.shl.com/.../python-new/",
  "description": "Multi-choice test...",
  "test_type": "K",
  "adaptive_support": "No",
  "remote_support": "Yes",
  "duration": 30,
  "skills": ["python", "programming", "databases"]
}
```

**Test Type Categories:**
- **K**: Knowledge & Skills (technical assessments)
- **P**: Personality & Behavior (soft skills)
- **A**: Ability & Aptitude (cognitive tests)
- **C**: Competencies (professional skills)
- **B**: Biodata & Situational Judgment
- **S**: Simulations
- **D**: Development & 360
- **E**: Assessment Exercises

## Data Flow Diagram

```
┌─────────┐
│  User   │
└────┬────┘
     │ 1. Enter query
     ▼
┌─────────────────┐
│   Frontend      │
│   (React)       │
└────┬────────────┘
     │ 2. POST /recommend
     │    {"query": "Java developer"}
     ▼
┌─────────────────┐
│   API           │
│   (FastAPI)     │
└────┬────────────┘
     │ 3. Call recommender
     ▼
┌─────────────────────────────────┐
│   Recommender                   │
│   ┌──────────────────────────┐ │
│   │ Query Analysis           │ │
│   │ → ["java", "developer"]  │ │
│   │ → Test types: [K]        │ │
│   └──────────────────────────┘ │
│              │                  │
│              ▼                  │
│   ┌──────────────────────────┐ │
│   │ Embedding                │ │
│   │ → [0.23, -0.45, ...]    │ │
│   └──────────────────────────┘ │
│              │                  │
│              ▼                  │
│   ┌──────────────────────────┐ │
│   │ Similarity Search        │ │
│   │ → Top 30 candidates      │ │
│   └──────────────────────────┘ │
│              │                  │
│              ▼                  │
│   ┌──────────────────────────┐ │
│   │ Balancing                │ │
│   │ → Select top 10          │ │
│   └──────────────────────────┘ │
└────┬────────────────────────────┘
     │ 4. Return recommendations
     ▼
┌─────────────────┐
│   API           │
│   Format JSON   │
└────┬────────────┘
     │ 5. HTTP Response
     ▼
┌─────────────────┐
│   Frontend      │
│   Display       │
└────┬────────────┘
     │ 6. Show results
     ▼
┌─────────┐
│  User   │
└─────────┘
```

## Deployment Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                    Cloud Platform                           │
│                                                             │
│  ┌──────────────────────┐      ┌──────────────────────┐  │
│  │  Frontend Service    │      │  Backend Service     │  │
│  │  (Vercel/Netlify)   │      │  (Render/Railway)    │  │
│  │                      │      │                      │  │
│  │  - Static files      │      │  - FastAPI app       │  │
│  │  - React build       │◄─────┤  - Recommender       │  │
│  │  - CDN distribution  │ API  │  - Embeddings        │  │
│  │                      │      │                      │  │
│  │  Port: 443 (HTTPS)   │      │  Port: 443 (HTTPS)   │  │
│  └──────────────────────┘      └──────────────────────┘  │
│           │                              │                 │
│           │                              │                 │
│           ▼                              ▼                 │
│  ┌──────────────────────┐      ┌──────────────────────┐  │
│  │  CDN Edge Nodes      │      │  Container Runtime   │  │
│  │  - Global caching    │      │  - Python 3.10       │  │
│  │  - Fast delivery     │      │  - Dependencies      │  │
│  └──────────────────────┘      └──────────────────────┘  │
└─────────────────────────────────────────────────────────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │  GitHub Repo    │
                    │  - Source code  │
                    │  - CI/CD        │
                    └─────────────────┘
```

## Security Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                    Security Layers                          │
│                                                             │
│  1. Transport Layer                                         │
│     ├─ HTTPS/TLS encryption                                │
│     └─ Secure headers                                       │
│                                                             │
│  2. Application Layer                                       │
│     ├─ Input validation (Pydantic)                         │
│     ├─ CORS configuration                                  │
│     ├─ Rate limiting (optional)                            │
│     └─ Error handling                                       │
│                                                             │
│  3. Data Layer                                              │
│     ├─ No sensitive data storage                           │
│     ├─ Read-only assessment data                           │
│     └─ No user authentication required                     │
└─────────────────────────────────────────────────────────────┘
```

## Performance Optimization

```
┌─────────────────────────────────────────────────────────────┐
│                  Performance Strategy                       │
│                                                             │
│  1. Pre-computation                                         │
│     └─ Embeddings computed at startup                      │
│                                                             │
│  2. In-Memory Storage                                       │
│     ├─ Assessment data in RAM                              │
│     └─ Embedding vectors in RAM                            │
│                                                             │
│  3. Efficient Algorithms                                    │
│     ├─ Vectorized operations (NumPy)                       │
│     └─ Optimized similarity computation                    │
│                                                             │
│  4. Caching (Future)                                        │
│     └─ Common queries cached                               │
│                                                             │
│  Result: < 500ms response time                             │
└─────────────────────────────────────────────────────────────┘
```

## Scalability Considerations

**Current Scale:**
- ~15-20 assessments
- Single instance
- In-memory processing

**Future Scale:**
- 1000+ assessments
- Multiple instances
- Vector database (Pinecone, Weaviate)
- Load balancing
- Caching layer (Redis)

**Scaling Path:**
```
Phase 1 (Current)
└─ Single instance, in-memory

Phase 2 (100+ assessments)
├─ Vector database
└─ Caching layer

Phase 3 (1000+ assessments)
├─ Multiple instances
├─ Load balancer
└─ CDN for static content

Phase 4 (10000+ assessments)
├─ Microservices architecture
├─ Distributed vector search
└─ Auto-scaling
```

## Monitoring & Observability

```
┌─────────────────────────────────────────────────────────────┐
│                    Monitoring Stack                         │
│                                                             │
│  Metrics:                                                   │
│  ├─ Response time                                          │
│  ├─ Error rate                                             │
│  ├─ Request count                                          │
│  └─ Recommendation quality                                 │
│                                                             │
│  Logging:                                                   │
│  ├─ API requests                                           │
│  ├─ Errors and exceptions                                  │
│  └─ Performance metrics                                    │
│                                                             │
│  Tracing (Future):                                         │
│  ├─ Request flow                                           │
│  ├─ Component latency                                      │
│  └─ Bottleneck identification                              │
└─────────────────────────────────────────────────────────────┘
```

---

This architecture provides a solid foundation for an intelligent, scalable, and maintainable assessment recommendation system.
