# Research Agent Project Report

## Abstract
This project presents a Goal-Based Multi-Agent System for automated researching and reporting. The Research Agent autonomously performs research on any given topic and generates a well-structured report. Upon receiving a user-specified concept, the system leverages web search tools to gather the most relevant and up-to-date information from the internet. It then processes and organizes this information into a comprehensive research report, including sections such as Introduction, Background, Objective, Methodology, Findings, Conclusion, and References. This approach enables students, professionals, and researchers to quickly produce detailed content on any subject.

The agent simulates the roles of a human researcher and writer using AI tools. It utilizes Serper to search Google and collect information, and Google Gemini to synthesize and write the report in natural language. CrewAI coordinates the workflow, managing the delegation of tasks between different agents (researcher and reporter). The final report is saved as a markdown file, ready for use or sharing.

## Project Overview
The Goal-Based Research Agent is designed to automate the process of information gathering, synthesis, and reporting. By combining multiple AI tools and APIs, the system provides a seamless experience for users who need comprehensive research reports with minimal effort.

## System Overview
The system is built with a modular Python codebase and integrates:
- **CrewAI** for multi-agent orchestration and task management
- **Serper API** for Google Search queries and online content retrieval
- **Google Gemini** for summarizing and generating the report
- **Streamlit** for a simple web-based user interface
- **Markdown** for storing the final structured output
- **Dotenv** for secure API key management
- **Requests** for API communication

## Design Methodology
- **Separation of Concerns:** Each component (search, report generation, UI, agent coordination) is encapsulated in its own module/class.
- **Goal-Based Task Delegation:** CrewAI manages the workflow, delegating research and reporting tasks to specialized agents.
- **API-Driven:** The system relies on external APIs for both search and AI, allowing for easy upgrades or replacements.
- **User-Centric:** The UI is minimal and focused on ease of use, requiring only a topic input.

## Algorithm Description
1. **Query Generation:** The agent generates a set of diverse search queries for the given topic to maximize coverage.
2. **Web Search:** Each query is sent to the Serper API, and results are formatted and aggregated.
3. **Report Generation:** Aggregated search results and the topic are sent as a prompt to Google Gemini, which returns a detailed markdown report.
4. **Report Cleaning:** The markdown output is cleaned of any code block markers for proper display and saving.
5. **Report Saving:** The report is saved in the `reports/` directory with a timestamped filename.

## Design and Implementation
- **Language:** Python 3.8+
- **Key Libraries:** `requests`, `streamlit`, `python-dotenv`, `google-genai`, `crewai`
- **Structure:**
  - `utils/agent.py`: Main agent logic and CrewAI integration
  - `utils/serper_api.py`: Web search API integration
  - `utils/gemini_agent.py`: Google Gemini integration
  - `app.py`: Streamlit UI
  - `main.py`: CLI entry point

## System Architecture
```
+-------------------+
|   User Interface  |
| (Streamlit/CLI)   |
+--------+----------+
         |
         v
+--------+----------+
|   ResearchAgent   |
+--------+----------+
         |
   +-----+-----+
   |           |
   v           v
SerperAPI   GeminiAgent
(Web Search) (Report Gen)
         |
         v
      CrewAI
 (Task Delegation)
```

## Implementation Workflow
1. User enters a topic via the UI or CLI.
2. The agent generates multiple search queries.
3. Each query is sent to the Serper API; results are formatted and aggregated.
4. Aggregated results and the topic are sent to Gemini for report generation.
5. The markdown report is cleaned and saved.
6. The report is displayed to the user in the UI and saved in the `reports/` directory.

## Results
- The system produces detailed, well-structured markdown reports on a wide range of topics.
- Reports are saved automatically and can be easily shared or published.
- The UI is intuitive and requires minimal user input.
- CrewAI enables future expansion to more complex, multi-agent workflows.

## Conclusion
The Goal-Based Research Agent automates the process of information gathering and synthesis, making research faster, more reliable, and accessible. Its modular, agent-based design allows for easy extension and integration with other APIs or AI models. The use of CrewAI provides a foundation for more advanced, collaborative research workflows in the future.

## Scope for Future Work
- **Multi-Agent Collaboration:** Deeper integration with CrewAI for complex, multi-step research workflows.
- **Support for Additional LLMs:** Allow users to select from multiple AI providers (e.g., OpenAI, Gemini, local models).
- **Advanced Query Generation:** Use NLP to generate even more targeted search queries.
- **Summarization and Highlighting:** Add features for summarizing or highlighting key findings in the report.
- **User Accounts and History:** Enable saving and retrieving past research sessions.

## Bibliography
- [Serper API Documentation](https://serper.dev/)
- [Google Gemini API Documentation](https://ai.google.dev/)
- [Streamlit Documentation](https://docs.streamlit.io/)
- [CrewAI Documentation](https://docs.crewai.com/)
- [Python Official Documentation](https://docs.python.org/3/)
