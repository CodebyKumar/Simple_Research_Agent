from datetime import datetime

class GeminiAgent:
    def __init__(self, google_api_key):
        from google import genai
        self.client = genai.Client(api_key=google_api_key)

    def generate_report(self, search_results: str, topic: str) -> str:
        prompt = (
            f"Create a comprehensive research report on the topic: \"{topic}\"\n\n"
            "Use the web search results provided below to create a detailed, well-structured report.\n\n"
            "REPORT STRUCTURE:\n"
            "1. Executive Summary\n2. Introduction\n3. Background\n4. Objective\n5. Methodology\n6. Findings\n7. Conclusion\n8. References\n\n"
            "FORMATTING REQUIREMENTS:\n"
            "- Use proper markdown formatting\n"
            "- Include clear headings and subheadings\n"
            "- Write in a professional, academic tone\n"
            "- Synthesize information from multiple sources\n"
            "- Provide specific examples and data points\n"
            "- Keep paragraphs well-structured and readable\n"
            "- Include actionable insights and recommendations\n\n"
            f"WEB SEARCH RESULTS:\n{search_results}\n\n"
            "Generate a comprehensive report that synthesizes all the information above into a coherent, professional document."
        )
        response = self.client.models.generate_content(
            model="gemini-2.0-flash-exp",
            contents=prompt
        )
        return response.text
