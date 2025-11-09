"""
FastAPI Application for SHL Assessment Recommendation System
"""
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional
import uvicorn
from recommender import AssessmentRecommender

app = FastAPI(title="SHL Assessment Recommendation API")

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize recommender
recommender = AssessmentRecommender()


class RecommendRequest(BaseModel):
    query: str


class AssessmentRecommendation(BaseModel):
    url: str
    name: str
    adaptive_support: str
    description: str
    duration: Optional[int] = None
    remote_support: str
    test_type: List[str]


class RecommendResponse(BaseModel):
    recommended_assessments: List[AssessmentRecommendation]


@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy"}


@app.post("/recommend", response_model=RecommendResponse)
async def recommend_assessments(request: RecommendRequest):
    """
    Recommend assessments based on query
    Returns 5-10 most relevant assessments
    """
    try:
        if not request.query or len(request.query.strip()) == 0:
            raise HTTPException(status_code=400, detail="Query cannot be empty")
        
        # Get recommendations
        recommendations = recommender.recommend(request.query, top_k=10)
        
        # Ensure minimum 5 recommendations
        if len(recommendations) < 5:
            raise HTTPException(
                status_code=500, 
                detail="Unable to generate minimum 5 recommendations"
            )
        
        # Format response according to API spec
        formatted_recommendations = []
        for rec in recommendations:
            formatted_recommendations.append(
                AssessmentRecommendation(
                    url=rec['assessment_url'],
                    name=rec['assessment_name'],
                    adaptive_support=rec.get('adaptive_support', 'No'),
                    description=rec.get('description', ''),
                    duration=rec.get('duration'),
                    remote_support=rec.get('remote_support', 'Yes'),
                    test_type=rec.get('test_type', ['O'])
                )
            )
        
        return RecommendResponse(recommended_assessments=formatted_recommendations)
    
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
