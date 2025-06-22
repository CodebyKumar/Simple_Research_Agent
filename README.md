# Research Agent

A simple research automation tool that uses web search and Google Gemini to generate comprehensive research reports on any topic.

## Features
- Automated web search using Serper API
- AI-powered report generation using Google Gemini
- Markdown report output, ready for sharing or publishing
- Clean, modular Python codebase

## Requirements
- Python 3.8+
- [Serper API key](https://serper.dev/)
- [Google Gemini API key](https://ai.google.dev/)
- Install dependencies:

```sh
pip install -r requirements.txt
```

## Setup
1. Clone this repository.
2. Create a `.env` file in the project root with the following content:
   ```env
   SERPER_API_KEY=your_serper_api_key_here
   GOOGLE_API_KEY=your_google_gemini_api_key_here
   ```
3. (Optional) Create a `reports/` directory, or let the script create it automatically.

## Usage
Run the research agent from the command line:

```sh
python main.py "Your research topic here"
```

### Example
```sh
python main.py "The Impact of Artificial Intelligence on the Future of Work"
```

The generated report will be saved in the `reports/` directory as a Markdown file.

## Output
- The report is saved as a clean Markdown file (no code block markers).
- Example output file: `reports/research_report_The_Impact_of_Artificial_Intelligence_on_the_Futur_20250614_222627.md`

## Project Structure
```
main.py
requirements.txt
reports/
utils/
    agent.py
    gemini_agent.py
    serper_api.py
    helpers.py
```

## Notes
- Make sure your API keys are valid and have sufficient quota.
- The tool does not log or save any information except the generated report.
- If you encounter issues, check your `.env` file and API key validity.

## License
MIT