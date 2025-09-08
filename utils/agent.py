import os
from dotenv import load_dotenv
from .serper_api import SerperAPI
from .gemini_agent import GeminiAgent
from pathlib import Path
from datetime import datetime
from crewai import Agent as CrewAgent, Task as CrewTask, Crew

class ResearchAgent:
    def __init__(self, serper_api_key=None, google_api_key=None):
        # If keys are provided (e.g., from Streamlit), use them; else load from .env
        if serper_api_key and google_api_key:
            self.serper_api_key = serper_api_key
            self.google_api_key = google_api_key
        else:
            load_dotenv()
            self.serper_api_key = os.getenv('SERPER_API_KEY')
            self.google_api_key = os.getenv('GOOGLE_API_KEY')
        if not self.serper_api_key:
            raise ValueError("SERPER_API_KEY not found in environment variables or input")
        if not self.google_api_key:
            raise ValueError("GOOGLE_API_KEY not found in environment variables or input")
        self.search_api = SerperAPI(self.serper_api_key)
        self.gemini_agent = GeminiAgent(self.google_api_key)

    def generate_search_queries(self, topic):
        # Generate a list of diverse queries for comprehensive research
        base = topic.strip()
        return [
            base,
            f"{base} latest developments 2024 2025",
            f"{base} research studies recent",
            f"{base} applications examples",
            f"{base} challenges limitations",
            f"{base} future trends"
        ]

    def conduct_search(self, topic):
        # Run all queries and aggregate formatted results
        search_queries = self.generate_search_queries(topic)
        all_results = []
        for i, query in enumerate(search_queries, 1):
            results = self.search_api.search(query)
            if results:
                formatted = self.search_api.format_results(results)
                all_results.append(f"\nSEARCH QUERY {i}: {query}\n{'='*60}\n{formatted}")
        return "\n".join(all_results) if all_results else "No search results obtained"

    def save_report(self, content, topic):
        # Clean up markdown/code block markers and whitespace
        content = content.strip()
        for marker in ('```markdown', '```'):
            if content.startswith(marker):
                content = content[len(marker):].lstrip('\n')
        if content.endswith('```'):
            content = content[:-3].rstrip('\n')
        # Save to file
        reports_dir = Path("reports")
        reports_dir.mkdir(exist_ok=True)
        clean_topic = "".join(c for c in topic if c.isalnum() or c in (' ', '-', '_')).strip().replace(' ', '_')[:50]
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = reports_dir / f"research_report_{clean_topic}_{timestamp}.md"
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Report saved to: {filename}")
        return filename

    def run_research(self, topic):
        """Conducts search and generates a report using Gemini."""
        search_results = self.conduct_search(topic)
        if not search_results or search_results == "No search results obtained":
            return "Research failed: Unable to obtain search results"
        report = self.gemini_agent.generate_report(search_results, topic)
        self.save_report(report, topic)
        return report

    def run_with_crewai(self, topic):
        """(Optional) CrewAI orchestration. Requires OpenAI API key unless CrewAI is configured for Gemini."""
        crew_agent = CrewAgent(
            name="ResearchAgent",
            role="researcher",
            description="Agent that conducts research using search APIs and Gemini.",
            goal=f"Research the topic: {topic}",
            backstory="A research assistant that leverages search APIs and Gemini to generate reports."
        )
        research_task = CrewTask(
            description=f"Conduct research and generate a report on: {topic}",
            expected_output="A detailed markdown report summarizing the research findings.",
            agent=crew_agent
        )
        crew = Crew(
            agents=[crew_agent],
            tasks=[research_task]
        )
        result = crew.kickoff()
        self.save_report(result, topic)
        return result
