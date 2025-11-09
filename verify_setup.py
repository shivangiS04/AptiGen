"""
Verify project setup and dependencies
"""
import os
import sys
import json

def check_file(path, description):
    """Check if a file exists"""
    if os.path.exists(path):
        print(f"✓ {description}")
        return True
    else:
        print(f"✗ {description} - MISSING")
        return False

def check_directory(path, description):
    """Check if a directory exists"""
    if os.path.isdir(path):
        print(f"✓ {description}")
        return True
    else:
        print(f"✗ {description} - MISSING")
        return False

def check_json_file(path, description):
    """Check if JSON file is valid"""
    if not os.path.exists(path):
        print(f"✗ {description} - MISSING")
        return False
    
    try:
        with open(path, 'r') as f:
            data = json.load(f)
        print(f"✓ {description} ({len(data)} items)")
        return True
    except Exception as e:
        print(f"✗ {description} - INVALID: {e}")
        return False

def main():
    print("🔍 Verifying SHL Assessment Recommendation System Setup")
    print("=" * 60)
    print()
    
    all_good = True
    
    # Check backend files
    print("Backend Files:")
    all_good &= check_file("backend/app.py", "API application")
    all_good &= check_file("backend/recommender.py", "Recommendation engine")
    all_good &= check_file("backend/scraper.py", "Web scraper")
    all_good &= check_file("backend/requirements.txt", "Backend dependencies")
    print()
    
    # Check frontend files
    print("Frontend Files:")
    all_good &= check_file("frontend/package.json", "Frontend package.json")
    all_good &= check_file("frontend/src/App.js", "React App component")
    all_good &= check_file("frontend/src/App.css", "App styles")
    all_good &= check_file("frontend/public/index.html", "HTML template")
    print()
    
    # Check data files
    print("Data Files:")
    all_good &= check_json_file("data/assessments.json", "Assessment catalog")
    all_good &= check_file("data/train_labeled.csv", "Training data")
    all_good &= check_file("data/test_unlabeled.csv", "Test data")
    print()
    
    # Check evaluation
    print("Evaluation:")
    all_good &= check_file("evaluation/evaluate.py", "Evaluation script")
    print()
    
    # Check documentation
    print("Documentation:")
    all_good &= check_file("README.md", "README")
    all_good &= check_file("APPROACH.md", "Approach document")
    all_good &= check_file("DEPLOYMENT.md", "Deployment guide")
    print()
    
    # Check scripts
    print("Scripts:")
    all_good &= check_file("test_api.py", "API test script")
    all_good &= check_file("run.sh", "Unix run script")
    all_good &= check_file("run.bat", "Windows run script")
    print()
    
    # Summary
    print("=" * 60)
    if all_good:
        print("✅ All checks passed! Your project is ready.")
        print()
        print("Next steps:")
        print("1. Run: ./run.sh (Unix/Mac) or run.bat (Windows)")
        print("2. In another terminal: cd frontend && npm install && npm start")
        print("3. Test API: python test_api.py")
        print("4. Generate predictions: cd evaluation && python evaluate.py")
    else:
        print("❌ Some files are missing. Please check the output above.")
        sys.exit(1)

if __name__ == "__main__":
    main()
