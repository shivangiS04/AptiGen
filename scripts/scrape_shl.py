"""
Enhanced SHL Scraper with better parsing
Run this to scrape actual SHL catalog data
"""
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'backend'))

from scraper import SHLScraper
import json

def main():
    print("Starting SHL catalog scraping...")
    print("This may take a few minutes...\n")
    
    scraper = SHLScraper()
    
    # Scrape the catalog
    assessments = scraper.scrape_catalog()
    
    if len(assessments) == 0:
        print("Warning: No assessments found. Using sample data.")
        print("You may need to manually inspect the SHL website structure")
        print("and update the scraper.py selectors.\n")
        
        # Create sample data
        assessments = create_sample_data()
    
    # Save to file
    output_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'assessments.json')
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(assessments, f, indent=2, ensure_ascii=False)
    
    print(f"\n✓ Saved {len(assessments)} assessments to {output_path}")
    
    # Print summary
    print("\nAssessment Summary:")
    test_types = {}
    for assessment in assessments:
        tt = assessment.get('test_type', 'Unknown')
        test_types[tt] = test_types.get(tt, 0) + 1
    
    for tt, count in sorted(test_types.items()):
        print(f"  {tt}: {count} assessments")

def create_sample_data():
    """Create comprehensive sample data based on SHL catalog"""
    return [
        {
            "name": "Python (New)",
            "url": "https://www.shl.com/solutions/products/product-catalog/view/python-new/",
            "description": "Multi-choice test that measures the knowledge of Python programming, databases, modules and library. For junior to mid-level roles.",
            "test_type": "K",
            "adaptive_support": "No",
            "remote_support": "Yes",
            "duration": 30,
            "skills": ["python", "programming", "databases", "technical"]
        },
        {
            "name": "Java Programming Assessment",
            "url": "https://www.shl.com/solutions/products/product-catalog/view/java/",
            "description": "Evaluates Java programming skills including OOP concepts, data structures, and algorithms. Suitable for developer roles.",
            "test_type": "K",
            "adaptive_support": "No",
            "remote_support": "Yes",
            "duration": 40,
            "skills": ["java", "programming", "technical", "oop"]
        },
        {
            "name": "SQL Assessment",
            "url": "https://www.shl.com/solutions/products/product-catalog/view/sql/",
            "description": "Tests SQL query writing, database design, and data manipulation skills for data-focused roles.",
            "test_type": "K",
            "adaptive_support": "No",
            "remote_support": "Yes",
            "duration": 35,
            "skills": ["sql", "database", "technical", "data"]
        },
        {
            "name": "JavaScript Assessment",
            "url": "https://www.shl.com/solutions/products/product-catalog/view/javascript/",
            "description": "Measures JavaScript programming knowledge including ES6+, async programming, and DOM manipulation.",
            "test_type": "K",
            "adaptive_support": "No",
            "remote_support": "Yes",
            "duration": 35,
            "skills": ["javascript", "programming", "technical", "web", "frontend"]
        },
        {
            "name": "Technology Professional 8.0 Job Focused Assessment",
            "url": "https://www.shl.com/solutions/products/product-catalog/view/technology-professional-8-0-job-focused-assessment/",
            "description": "The Technology Job Focused Assessment assesses key behavioral attributes required for success in fast-paced technology roles.",
            "test_type": "P",
            "adaptive_support": "No",
            "remote_support": "Yes",
            "duration": 45,
            "skills": ["competencies", "personality", "behavior", "technology"]
        },
        {
            "name": "Teamwork and Collaboration Assessment",
            "url": "https://www.shl.com/solutions/products/product-catalog/view/teamwork/",
            "description": "Measures ability to work effectively in teams and collaborate with stakeholders across the organization.",
            "test_type": "P",
            "adaptive_support": "No",
            "remote_support": "Yes",
            "duration": 25,
            "skills": ["teamwork", "collaboration", "communication", "interpersonal"]
        },
        {
            "name": "Leadership Assessment",
            "url": "https://www.shl.com/solutions/products/product-catalog/view/leadership/",
            "description": "Evaluates leadership competencies including strategic thinking, decision-making, and people management.",
            "test_type": "P",
            "adaptive_support": "No",
            "remote_support": "Yes",
            "duration": 30,
            "skills": ["leadership", "management", "decision-making", "strategic"]
        },
        {
            "name": "Verify Cognitive Ability",
            "url": "https://www.shl.com/solutions/products/product-catalog/view/verify-cognitive-ability/",
            "description": "Measures general cognitive ability including numerical, verbal, and inductive reasoning.",
            "test_type": "A",
            "adaptive_support": "Yes",
            "remote_support": "Yes",
            "duration": 20,
            "skills": ["cognitive", "analytical", "reasoning", "problem-solving"]
        },
        {
            "name": "Communication Skills Assessment",
            "url": "https://www.shl.com/solutions/products/product-catalog/view/communication/",
            "description": "Assesses written and verbal communication effectiveness in professional contexts.",
            "test_type": "C",
            "adaptive_support": "No",
            "remote_support": "Yes",
            "duration": 30,
            "skills": ["communication", "writing", "presentation", "verbal"]
        },
        {
            "name": "Numerical Reasoning",
            "url": "https://www.shl.com/solutions/products/product-catalog/view/numerical-reasoning/",
            "description": "Tests ability to work with numerical data, interpret charts, and perform calculations.",
            "test_type": "A",
            "adaptive_support": "Yes",
            "remote_support": "Yes",
            "duration": 25,
            "skills": ["numerical", "analytical", "data-analysis", "quantitative"]
        },
        {
            "name": "Verbal Reasoning",
            "url": "https://www.shl.com/solutions/products/product-catalog/view/verbal-reasoning/",
            "description": "Evaluates ability to understand and analyze written information and draw logical conclusions.",
            "test_type": "A",
            "adaptive_support": "Yes",
            "remote_support": "Yes",
            "duration": 25,
            "skills": ["verbal", "analytical", "comprehension", "logical"]
        },
        {
            "name": "Customer Service Skills",
            "url": "https://www.shl.com/solutions/products/product-catalog/view/customer-service/",
            "description": "Measures customer service orientation, empathy, and problem-solving in service contexts.",
            "test_type": "C",
            "adaptive_support": "No",
            "remote_support": "Yes",
            "duration": 30,
            "skills": ["customer-service", "empathy", "communication", "problem-solving"]
        },
        {
            "name": "Strategic Thinking Assessment",
            "url": "https://www.shl.com/solutions/products/product-catalog/view/strategic-thinking/",
            "description": "Evaluates ability to think strategically, analyze complex situations, and make informed decisions.",
            "test_type": "C",
            "adaptive_support": "No",
            "remote_support": "Yes",
            "duration": 35,
            "skills": ["strategic", "analytical", "decision-making", "planning"]
        },
        {
            "name": "Situational Judgment Test",
            "url": "https://www.shl.com/solutions/products/product-catalog/view/situational-judgment/",
            "description": "Presents realistic workplace scenarios to assess judgment and decision-making in context.",
            "test_type": "B",
            "adaptive_support": "No",
            "remote_support": "Yes",
            "duration": 30,
            "skills": ["judgment", "decision-making", "situational", "workplace"]
        },
        {
            "name": "Cloud Computing Knowledge",
            "url": "https://www.shl.com/solutions/products/product-catalog/view/cloud-computing/",
            "description": "Tests knowledge of cloud platforms, services, and infrastructure concepts.",
            "test_type": "K",
            "adaptive_support": "No",
            "remote_support": "Yes",
            "duration": 35,
            "skills": ["cloud", "devops", "infrastructure", "technical", "aws", "azure"]
        }
    ]

if __name__ == "__main__":
    main()
