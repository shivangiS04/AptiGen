"""
Evaluation script for SHL Assessment Recommendation System
Calculates Mean Recall@K on test set
"""
import pandas as pd
import numpy as np
from typing import List, Dict
import sys
import os

# Add parent directory to path
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'backend'))
from recommender import AssessmentRecommender


def load_labeled_data(filepath: str) -> List[Dict]:
    """Load labeled training/test data"""
    df = pd.read_csv(filepath)
    
    queries = []
    for query_text in df['query'].unique():
        query_data = df[df['query'] == query_text]
        relevant_urls = query_data['assessment_url'].tolist()
        queries.append({
            'query': query_text,
            'relevant_urls': relevant_urls
        })
    
    return queries


def calculate_recall_at_k(recommended_urls: List[str], 
                          relevant_urls: List[str], 
                          k: int = 10) -> float:
    """Calculate Recall@K for a single query"""
    recommended_set = set(recommended_urls[:k])
    relevant_set = set(relevant_urls)
    
    if len(relevant_set) == 0:
        return 0.0
    
    intersection = recommended_set & relevant_set
    recall = len(intersection) / len(relevant_set)
    
    return recall


def evaluate_recommender(recommender: AssessmentRecommender,
                        test_queries: List[Dict],
                        k: int = 10) -> Dict:
    """Evaluate recommender on test set"""
    recalls = []
    results = []
    
    for item in test_queries:
        query = item['query']
        relevant_urls = item['relevant_urls']
        
        # Get recommendations
        recommendations = recommender.recommend(query, top_k=k)
        recommended_urls = [r['assessment_url'] for r in recommendations]
        
        # Calculate recall
        recall = calculate_recall_at_k(recommended_urls, relevant_urls, k)
        recalls.append(recall)
        
        results.append({
            'query': query,
            'recall@10': recall,
            'num_relevant': len(relevant_urls),
            'num_found': len(set(recommended_urls) & set(relevant_urls))
        })
    
    mean_recall = np.mean(recalls)
    
    return {
        'mean_recall@10': mean_recall,
        'individual_results': results
    }


def generate_submission_csv(recommender: AssessmentRecommender,
                           test_queries_file: str,
                           output_file: str = 'predictions.csv'):
    """Generate submission CSV for unlabeled test set"""
    # Load test queries (just query column, no labels)
    df = pd.read_csv(test_queries_file)
    
    submission_data = []
    
    for query in df['query']:
        recommendations = recommender.recommend(query, top_k=10)
        
        for rec in recommendations:
            submission_data.append({
                'Query': query,
                'Assessment_url': rec['assessment_url']
            })
    
    # Save to CSV
    submission_df = pd.DataFrame(submission_data)
    submission_df.to_csv(output_file, index=False)
    print(f"Submission CSV saved to {output_file}")
    
    return submission_df


if __name__ == "__main__":
    # Initialize recommender
    recommender = AssessmentRecommender('../data/assessments.json')
    
    # Evaluate on labeled train set
    print("Evaluating on labeled train set...")
    train_queries = load_labeled_data('../data/train_labeled.csv')
    results = evaluate_recommender(recommender, train_queries, k=10)
    
    print(f"\nMean Recall@10: {results['mean_recall@10']:.4f}")
    print("\nIndividual Results:")
    for r in results['individual_results']:
        print(f"Query: {r['query'][:50]}...")
        print(f"  Recall@10: {r['recall@10']:.4f} ({r['num_found']}/{r['num_relevant']} found)")
    
    # Generate submission for unlabeled test set
    print("\n\nGenerating submission CSV...")
    generate_submission_csv(
        recommender,
        '../data/test_unlabeled.csv',
        '../predictions.csv'
    )
