"""
Quick test to verify recommendations are working correctly
"""
import sys
sys.path.append('backend')

from recommender import AssessmentRecommender

# Initialize recommender
print("Initializing recommender...")
recommender = AssessmentRecommender('data/assessments.json')
print(f"Loaded {len(recommender.assessments)} assessments\n")

# Test different queries
test_queries = [
    "Java developer",
    "Python programmer",
    "Leadership and teamwork",
    "Analytical thinking",
    "SQL database expert"
]

for query in test_queries:
    print(f"\n{'='*60}")
    print(f"Query: {query}")
    print('='*60)
    
    results = recommender.recommend(query, top_k=5)
    
    for i, rec in enumerate(results, 1):
        print(f"{i}. {rec['assessment_name']}")
        print(f"   Type: {rec['test_type']}")
        print(f"   Score: {rec['relevance_score']:.4f}")
    
    print()

print("\n" + "="*60)
print("If you see different assessments for different queries,")
print("the recommender is working correctly!")
print("="*60)
