"""
Test script for API endpoints
"""
import requests
import json

API_URL = "http://localhost:8000"

def test_health():
    """Test health endpoint"""
    print("Testing /health endpoint...")
    response = requests.get(f"{API_URL}/health")
    print(f"Status: {response.status_code}")
    print(f"Response: {response.json()}")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"
    print("✓ Health check passed\n")

def test_recommend():
    """Test recommend endpoint"""
    print("Testing /recommend endpoint...")
    
    test_queries = [
        "I am hiring for Java developers who can also collaborate effectively with my business teams.",
        "Looking to hire mid-level professionals who are proficient in Python, SQL and JavaScript.",
        "Need assessments for an analyst role with cognitive and personality tests."
    ]
    
    for query in test_queries:
        print(f"\nQuery: {query[:60]}...")
        response = requests.post(
            f"{API_URL}/recommend",
            json={"query": query}
        )
        
        print(f"Status: {response.status_code}")
        
        if response.status_code == 200:
            data = response.json()
            assessments = data["recommended_assessments"]
            print(f"Number of recommendations: {len(assessments)}")
            
            # Check minimum 5 recommendations
            assert len(assessments) >= 5, "Should return at least 5 recommendations"
            assert len(assessments) <= 10, "Should return at most 10 recommendations"
            
            # Check required fields
            for i, assessment in enumerate(assessments[:3], 1):
                print(f"\n  {i}. {assessment['name']}")
                print(f"     Type: {assessment['test_type']}")
                print(f"     URL: {assessment['url']}")
                
                # Validate required fields
                assert 'url' in assessment
                assert 'name' in assessment
                assert 'adaptive_support' in assessment
                assert 'description' in assessment
                assert 'remote_support' in assessment
                assert 'test_type' in assessment
                assert isinstance(assessment['test_type'], list)
            
            print(f"\n✓ Recommendation test passed for this query")
        else:
            print(f"Error: {response.text}")
            raise Exception("Recommendation endpoint failed")

def test_response_format():
    """Test exact response format"""
    print("\n\nTesting response format compliance...")
    
    response = requests.post(
        f"{API_URL}/recommend",
        json={"query": "Java developer"}
    )
    
    data = response.json()
    
    # Check top-level structure
    assert "recommended_assessments" in data
    assert isinstance(data["recommended_assessments"], list)
    
    # Check assessment structure
    if len(data["recommended_assessments"]) > 0:
        assessment = data["recommended_assessments"][0]
        required_fields = ["url", "name", "adaptive_support", "description", 
                          "remote_support", "test_type"]
        
        for field in required_fields:
            assert field in assessment, f"Missing required field: {field}"
        
        # Check types
        assert isinstance(assessment["url"], str)
        assert isinstance(assessment["name"], str)
        assert isinstance(assessment["adaptive_support"], str)
        assert isinstance(assessment["description"], str)
        assert isinstance(assessment["remote_support"], str)
        assert isinstance(assessment["test_type"], list)
        
        print("✓ Response format is compliant")

if __name__ == "__main__":
    try:
        test_health()
        test_recommend()
        test_response_format()
        print("\n" + "="*50)
        print("ALL TESTS PASSED ✓")
        print("="*50)
    except Exception as e:
        print(f"\n❌ TEST FAILED: {e}")
        exit(1)
