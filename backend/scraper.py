"""
SHL Assessment Catalog Scraper
Scrapes individual test solutions from SHL's product catalog
"""
import requests
from bs4 import BeautifulSoup
import json
import time
from typing import List, Dict
import re


class SHLScraper:
    def __init__(self):
        self.base_url = "https://www.shl.com/solutions/products/product-catalog/"
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        
    def scrape_catalog(self) -> List[Dict]:
        """Scrape all individual test solutions from SHL catalog"""
        assessments = []
        
        try:
            response = requests.get(self.base_url, headers=self.headers, timeout=30)
            response.raise_for_status()
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Find assessment cards/links (adjust selectors based on actual HTML)
            # This is a template - you'll need to inspect the actual page structure
            assessment_links = soup.find_all('a', href=True)
            
            for link in assessment_links:
                href = link.get('href', '')
                # Filter for individual test solutions
                if 'product' in href.lower() or 'assessment' in href.lower():
                    if 'pre-packaged' not in href.lower():
                        assessment_data = self._scrape_assessment_page(href)
                        if assessment_data:
                            assessments.append(assessment_data)
                            time.sleep(0.5)  # Be respectful
                            
        except Exception as e:
            print(f"Error scraping catalog: {e}")
            
        return assessments
    
    def _scrape_assessment_page(self, url: str) -> Dict:
        """Scrape individual assessment page for details"""
        try:
            if not url.startswith('http'):
                url = 'https://www.shl.com' + url
                
            response = requests.get(url, headers=self.headers, timeout=30)
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Extract assessment details
            title = soup.find('h1')
            title_text = title.get_text(strip=True) if title else ""
            
            # Extract description
            description = ""
            desc_elem = soup.find('div', class_='description') or soup.find('p')
            if desc_elem:
                description = desc_elem.get_text(strip=True)
            
            # Extract test type (K, P, etc.)
            test_type = self._extract_test_type(soup, description)
            
            return {
                'name': title_text,
                'url': url,
                'description': description,
                'test_type': test_type,
                'skills': self._extract_skills(soup, description)
            }
            
        except Exception as e:
            print(f"Error scraping {url}: {e}")
            return None
    
    def _extract_test_type(self, soup, description: str) -> str:
        """Extract test type (K=Knowledge, P=Personality, etc.)"""
        text = description.lower()
        if 'personality' in text or 'behavior' in text:
            return 'P'
        elif 'cognitive' in text or 'ability' in text:
            return 'C'
        elif 'knowledge' in text or 'skill' in text or 'technical' in text:
            return 'K'
        return 'O'  # Other
    
    def _extract_skills(self, soup, description: str) -> List[str]:
        """Extract relevant skills from assessment description"""
        skills = []
        # Common skill keywords
        skill_keywords = [
            'java', 'python', 'sql', 'javascript', 'leadership',
            'communication', 'analytical', 'problem-solving', 'teamwork'
        ]
        
        text = description.lower()
        for skill in skill_keywords:
            if skill in text:
                skills.append(skill)
                
        return skills
    
    def save_to_file(self, assessments: List[Dict], filename: str = 'assessments.json'):
        """Save scraped assessments to JSON file"""
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(assessments, f, indent=2, ensure_ascii=False)
        print(f"Saved {len(assessments)} assessments to {filename}")


if __name__ == "__main__":
    scraper = SHLScraper()
    assessments = scraper.scrape_catalog()
    scraper.save_to_file(assessments, '../data/assessments.json')
