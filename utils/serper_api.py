import requests
import json
import logging
from typing import Dict, Optional

class SerperAPI:
    def __init__(self, api_key: str):
        if not api_key:
            raise ValueError("Serper API key is required.")
        self.api_key = api_key
        self.endpoint = "https://google.serper.dev/search"
        logging.basicConfig(level=logging.INFO)

    def search(self, query: str, max_results: int = 10) -> dict:
        """
        Performs a search using the Serper API and returns the results.
        """
        payload = json.dumps({"q": query, "num": max_results})
        headers = {'X-API-KEY': self.api_key, 'Content-Type': 'application/json'}
        
        try:
            response = requests.post(self.endpoint, headers=headers, data=payload)
            response.raise_for_status()  # Raises an HTTPError for bad responses (4XX or 5XX)
            return response.json()
        except requests.exceptions.RequestException as e:
            logging.error(f"An error occurred during Serper API request: {e}")
            return {}

    def format_results(self, results: dict) -> str:
        """
        Formats the search results into a readable string.
        """
        if not results or 'organic' not in results:
            return "No results found."
        
        formatted_output = []
        for item in results['organic']:
            title = item.get('title', 'No Title')
            link = item.get('link', '#')
            snippet = item.get('snippet', 'No snippet available.')
            formatted_output.append(f"Title: {title}\nLink: {link}\nSnippet: {snippet}\n---")
            
        return "\n".join(formatted_output)
