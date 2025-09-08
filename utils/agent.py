import os
from dotenv import load_dotenv
from .serper_api import SerperAPI
from .gemini_agent import GeminiAgent
from .helpers import get_filename_from_topic
from pathlib import Path
from datetime import datetime
import logging

class ResearchAgent:
    def __init__(self, serper_api_key: str = None, google_api_key: str = None):
        load_dotenv()
        self.serper_api_key = serper_api_key or os.getenv('SERPER_API_KEY')
        self.google_api_key = google_api_key or os.getenv('GOOGLE_API_KEY')

        if not self.serper_api_key or not self.google_api_key:
            raise ValueError("API keys for Serper and Google must be provided or set in .env")

        self.search_api = SerperAPI(self.serper_api_key)
        self.gemini_agent = GeminiAgent(self.google_api_key)
        logging.basicConfig(level=logging.INFO)

    def generate_search_queries(self, topic: str) -> list[str]:
        """Generates a diverse list of search queries for a given topic."""
        base = topic.strip()
        return [
            base,
            f"{base} recent developments",
            f"{base} key challenges",
            f"{base} future outlook",
            f"{base} applications",
        ]

    def conduct_search(self, topic: str) -> str:
        """Conducts searches for all generated queries and returns a formatted string."""
        queries = self.generate_search_queries(topic)
        all_results = []
        for query in queries:
            logging.info(f"Searching for: {query}")
            results = self.search_api.search(query)
            if results:
                formatted = self.search_api.format_results(results)
                all_results.append(f"Search Query: {query}\n{'-'*20}\n{formatted}")
        return "\n\n".join(all_results) or "No search results found."

    def save_report(self, content: str, topic: str) -> Path:
        """Saves the research report to a file in the 'reports' directory."""
        reports_dir = Path("reports")
        reports_dir.mkdir(exist_ok=True)
        
        clean_topic = get_filename_from_topic(topic)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = reports_dir / f"report_{clean_topic}_{timestamp}.md"
        
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
        logging.info(f"Report saved to {filename}")
        return filename

    def run_research(self, topic: str) -> str:
        """Main method to run the research, generate, and save a report."""
        logging.info(f"Starting research on: {topic}")
        search_results = self.conduct_search(topic)
        if "No search results" in search_results:
            return "Could not retrieve search results. Please check API keys and network."
        
        report = self.gemini_agent.generate_report(search_results, topic)
        self.save_report(report, topic)
        return report
