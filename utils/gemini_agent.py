import google.generativeai as genai
import logging

class GeminiAgent:
    def __init__(self, api_key: str):
        if not api_key:
            raise ValueError("Google Gemini API key is required.")
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel('gemini-pro')
        logging.basicConfig(level=logging.INFO)

    def generate_report(self, search_results: str, topic: str) -> str:
        """
        Generates a research report using the Gemini model based on search results.
        """
        prompt = f"""
        You are a professional researcher. Your task is to generate a comprehensive,
        well-structured, and easy-to-understand research report in Markdown format.

        **Topic:** {topic}

        Please use the following search results to draft the report. Synthesize the 
        information, identify key findings, and present them in a clear and organized 
        manner. Do not just copy-paste the content.

        **Search Results:**
        {search_results}

        **Report Structure:**
        1.  **Introduction:** A brief overview of the topic and report scope.
        2.  **Key Findings:** Main points, data, and discoveries from the research. 
            (Use bullet points for clarity).
        3.  **Applications/Examples:** Real-world applications or examples, if applicable.
        4.  **Challenges/Limitations:** Any known challenges, limitations, or controversies.
        5.  **Future Trends:** Potential future developments and trends.
        6.  **Conclusion:** A summary of the key takeaways.

        Begin generating the report now.
        """
        try:
            response = self.model.generate_content(prompt)
            # It's good practice to check if the response has the expected text attribute
            if hasattr(response, 'text'):
                return response.text
            else:
                # Handle cases where the response might not be as expected
                logging.error("Gemini response did not contain text.")
                return "Error: Failed to generate report due to an unexpected API response."
        except Exception as e:
            logging.error(f"An error occurred while generating the report with Gemini: {e}")
            return f"An error occurred: {e}"
