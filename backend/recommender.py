"""
Assessment Recommendation Engine
Uses semantic similarity and LLM for intelligent recommendations
"""
import json
import numpy as np
from typing import List, Dict, Optional
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import google.generativeai as genai
import os
from collections import defaultdict


class AssessmentRecommender:
    def __init__(self, assessments_path: str = None):
        self.model = None

        
        # Smart path resolution for different environments
        if assessments_path is None:
            assessments_path = self._find_assessments_file()
        
        self.assessments = self._load_assessments(assessments_path)
        self.embeddings = None
        
        # Initialize Gemini API
        api_key = os.getenv('GEMINI_API_KEY')
        if api_key:
            genai.configure(api_key=api_key)
            self.llm = genai.GenerativeModel('gemini-pro')
        else:
            self.llm = None
            
        self._build_index()
    
    def _find_assessments_file(self) -> str:
        """Find assessments.json in multiple possible locations"""
        possible_paths = [
            'data/assessments.json',      # Render deployment (backend/data/)
            '../data/assessments.json',   # Local development
            'assessments.json',            # Same directory
            './backend/data/assessments.json',  # From project root
        ]
        
        for path in possible_paths:
            if os.path.exists(path):
                print(f"✓ Found assessments at: {path}")
                return path
        
        print("⚠ Warning: assessments.json not found in any location. Using sample data.")
        return 'data/assessments.json'  # Default fallback
    
    def _load_assessments(self, path: str) -> List[Dict]:
        """Load assessments from JSON file"""
        try:
            with open(path, 'r', encoding='utf-8') as f:
                data = json.load(f)
                print(f"✓ Loaded {len(data)} assessments from {path}")
                return data
        except FileNotFoundError:
            print(f"⚠ Warning: {path} not found. Using sample data.")
            return self._get_sample_assessments()
        except Exception as e:
            print(f"⚠ Error loading {path}: {e}. Using sample data.")
            return self._get_sample_assessments()
    
    def _get_sample_assessments(self) -> List[Dict]:
        """Sample assessments for testing"""
        return [
            {
                'name': 'Java Programming Assessment',
                'url': 'https://www.shl.com/solutions/products/java-assessment',
                'description': 'Evaluates Java programming skills and knowledge',
                'test_type': 'K',
                'skills': ['java', 'programming', 'technical']
            },
            {
                'name': 'Teamwork and Collaboration Assessment',
                'url': 'https://www.shl.com/solutions/products/teamwork-assessment',
                'description': 'Measures ability to work effectively in teams',
                'test_type': 'P',
                'skills': ['teamwork', 'collaboration', 'communication']
            }
        ]

    def _build_index(self):
        """Build embeddings index for all assessments"""
        if self.model is None:
            from sentence_transformers import SentenceTransformer
            self.model = SentenceTransformer('paraphrase-MiniLM-L3-v2')

        texts = [
            f"{a['name']} {a['description']} {' '.join(a.get('skills', []))}"
            for a in self.assessments
        ]
        self.embeddings = self.model.encode(texts, convert_to_numpy=True, dtype=np.float16)


    def recommend(self, query: str, top_k: int = 10) -> List[Dict]:
        """
        Recommend assessments based on query
        Returns balanced recommendations across test types
        """
        # Get semantic similarity scores
        query_embedding = self.model.encode([query])
        similarities = cosine_similarity(query_embedding, self.embeddings)[0]
        
        # Debug: Print top similarities
        print(f"\n🔍 Query: {query}")
        print(f"📊 Top 5 similarity scores:")
        top_5_indices = np.argsort(similarities)[::-1][:5]
        for idx in top_5_indices:
            print(f"   {self.assessments[idx]['name']}: {similarities[idx]:.4f}")
        
        # Get top candidates (more than needed for balancing)
        top_indices = np.argsort(similarities)[::-1][:min(len(self.assessments), top_k * 3)]
        
        # Extract query requirements
        requirements = self._extract_requirements(query)
        print(f"🎯 Detected types: {requirements['test_types_needed']}")
        
        # Balance recommendations by test type
        recommendations = self._balance_recommendations(
            top_indices, similarities, requirements, top_k
        )
        
        return recommendations
    
    def _extract_requirements(self, query: str) -> Dict:
        """Extract skill and test type requirements from query"""
        requirements = {
            'technical_skills': [],
            'behavioral_skills': [],
            'test_types_needed': set()
        }
        
        query_lower = query.lower()
        
        # Technical skills (Knowledge & Skills - K)
        tech_keywords = ['java', 'python', 'sql', 'javascript', 'programming', 
                        'coding', 'technical', 'developer', 'engineer', 'software',
                        'database', 'web', 'frontend', 'backend', 'fullstack',
                        'react', 'node', 'angular', 'vue', 'django', 'flask',
                        'c++', 'c#', 'ruby', 'php', 'go', 'rust', 'kotlin', 'swift']
        for keyword in tech_keywords:
            if keyword in query_lower:
                requirements['technical_skills'].append(keyword)
                requirements['test_types_needed'].add('K')
        
        # Behavioral skills (Personality & Behavior - P)
        behavioral_keywords = ['collaborate', 'collaboration', 'teamwork', 'team', 
                              'communication', 'leadership', 'leader', 'personality', 
                              'behavior', 'interpersonal', 'social', 'management',
                              'manage', 'motivate', 'inspire', 'influence']
        for keyword in behavioral_keywords:
            if keyword in query_lower:
                requirements['behavioral_skills'].append(keyword)
                requirements['test_types_needed'].add('P')
        
        # Cognitive/Ability (Ability & Aptitude - A)
        cognitive_keywords = ['cognitive', 'analytical', 'problem-solving', 'reasoning',
                             'logic', 'critical thinking', 'aptitude', 'ability',
                             'numerical', 'verbal', 'abstract', 'spatial']
        for keyword in cognitive_keywords:
            if keyword in query_lower:
                requirements['test_types_needed'].add('A')
        
        # Competencies (C)
        competency_keywords = ['competenc', 'skill', 'strategic', 'planning',
                              'decision', 'judgment', 'professional']
        for keyword in competency_keywords:
            if keyword in query_lower:
                requirements['test_types_needed'].add('C')
        
        return requirements
    
    def _balance_recommendations(self, indices: np.ndarray, 
                                similarities: np.ndarray,
                                requirements: Dict, 
                                top_k: int) -> List[Dict]:
        """Balance recommendations across different test types"""
        recommendations = []
        seen_indices = set()
        test_type_counts = defaultdict(int)
        
        # Determine target distribution
        needed_types = requirements['test_types_needed']
        
        if len(needed_types) == 0:
            # No specific requirements, use top similarity scores
            for idx in indices[:top_k]:
                if idx not in seen_indices:
                    recommendations.append(self._format_recommendation(idx, similarities[idx]))
                    seen_indices.add(idx)
            # Remove internal index
            for rec in recommendations:
                rec.pop('_idx', None)
            return recommendations
        
        # Calculate slots per type
        slots_per_type = max(1, top_k // len(needed_types))
        
        # First pass: fill required types
        for idx in indices:
            if len(recommendations) >= top_k:
                break
            
            if idx in seen_indices:
                continue
                
            assessment = self.assessments[idx]
            test_type = assessment.get('test_type', 'O')
            
            if test_type in needed_types:
                if test_type_counts[test_type] < slots_per_type:
                    recommendations.append(self._format_recommendation(idx, similarities[idx]))
                    seen_indices.add(idx)
                    test_type_counts[test_type] += 1
        
        # Second pass: fill remaining slots with best matches
        for idx in indices:
            if len(recommendations) >= top_k:
                break
            if idx not in seen_indices:
                recommendations.append(self._format_recommendation(idx, similarities[idx]))
                seen_indices.add(idx)
        
        # Sort by relevance score BEFORE removing internal index
        recommendations.sort(key=lambda x: x['relevance_score'], reverse=True)
        
        # Remove internal index
        for rec in recommendations:
            rec.pop('_idx', None)
        
        print(f"✅ Returning {len(recommendations)} recommendations (sorted by relevance)\n")
        
        return recommendations[:top_k]
    
    def _format_recommendation(self, idx: int, score: float) -> Dict:
        """Format assessment as recommendation"""
        assessment = self.assessments[idx]
        test_type = assessment.get('test_type', 'O')
        # Convert single test_type to list if needed
        if isinstance(test_type, str):
            test_type = [test_type]
        
        return {
            'assessment_name': assessment['name'],
            'assessment_url': assessment['url'],
            'description': assessment.get('description', ''),
            'test_type': test_type,
            'adaptive_support': assessment.get('adaptive_support', 'No'),
            'remote_support': assessment.get('remote_support', 'Yes'),
            'duration': assessment.get('duration'),
            'relevance_score': float(score),
            '_idx': idx  # Internal use for deduplication
        }
    
    def evaluate_recall(self, test_queries: List[Dict], k: int = 10) -> float:
        """
        Evaluate Mean Recall@K on test set
        test_queries format: [{'query': '...', 'relevant_urls': [...]}]
        """
        recalls = []
        
        for item in test_queries:
            query = item['query']
            relevant_urls = set(item['relevant_urls'])
            
            recommendations = self.recommend(query, top_k=k)
            recommended_urls = set([r['assessment_url'] for r in recommendations])
            
            # Calculate recall
            if len(relevant_urls) > 0:
                recall = len(recommended_urls & relevant_urls) / len(relevant_urls)
                recalls.append(recall)
        
        return np.mean(recalls) if recalls else 0.0


if __name__ == "__main__":
    # Test the recommender
    recommender = AssessmentRecommender()
    
    test_query = "I need a Java developer who can collaborate with teams"
    results = recommender.recommend(test_query, top_k=5)
    
    print(f"Query: {test_query}\n")
    for i, rec in enumerate(results, 1):
        print(f"{i}. {rec['assessment_name']}")
        print(f"   Type: {rec['test_type']}, Score: {rec['relevance_score']:.3f}")
        print(f"   URL: {rec['assessment_url']}\n")
