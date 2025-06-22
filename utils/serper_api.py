import requests
import json
from typing import Dict, Optional

class SerperAPI:
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.base_url = "https://google.serper.dev"
        self.session = requests.Session()

    def search(self, query: str, num_results: int = 10) -> Optional[Dict]:
        url = f"{self.base_url}/search"
        payload = {
            "q": query,
            "num": num_results,
            "gl": "us",
            "hl": "en"
        }
        headers = {
            'X-API-KEY': self.api_key,
            'Content-Type': 'application/json'
        }
        response = self.session.post(
            url,
            headers=headers,
            data=json.dumps(payload),
            timeout=30
        )
        response.raise_for_status()
        return response.json()

    def format_results(self, results: Dict) -> str:
        if not results:
            return "No search results found."
        sections = []
        if 'organic' in results and results['organic']:
            sections.append("WEB SEARCH RESULTS\n" + "="*50)
            for i, result in enumerate(results['organic'][:10], 1):
                title = result.get('title', 'N/A')
                link = result.get('link', 'N/A')
                snippet = result.get('snippet', 'N/A')
                sections.append(f"""
Result {i}:
Title: {title}
URL: {link}
Summary: {snippet}
{'-' * 50}""")
        if 'knowledgeGraph' in results:
            kg = results['knowledgeGraph']
            sections.append(f"""
KNOWLEDGE GRAPH
{'-' * 50}
Title: {kg.get('title', 'N/A')}
Type: {kg.get('type', 'N/A')}
Description: {kg.get('description', 'N/A')}
{'-' * 50}""")
        if 'peopleAlsoAsk' in results and results['peopleAlsoAsk']:
            questions = [q.get('question', '') for q in results['peopleAlsoAsk'][:5] if q.get('question')]
            if questions:
                sections.append(f"""
PEOPLE ALSO ASK
{'-' * 50}
{chr(10).join(f"- {q}" for q in questions)}
{'-' * 50}""")
        return "\n".join(sections)
