from google import genai
import logging
import os

class GeminiAgent:
    def __init__(self, api_key: str = None):
        """
        Initializes the GeminiAgent.
        The API key is retrieved from the GOOGLE_API_KEY environment variable if not provided.
        """
        if api_key is None:
            api_key = os.environ.get("GOOGLE_API_KEY")
        if not api_key:
            raise ValueError("Google Gemini API key is required. Please provide it as an argument or set the GOOGLE_API_KEY environment variable.")
        
        # In the new SDK, a client is initialized to interact with the API.
        self.client = genai.Client(api_key=api_key)
        logging.basicConfig(level=logging.INFO)

    def generate_report(self, search_results: str, topic: str, model_name: str = "gemini-1.5-flash") -> str:
        """
        Generates a research report using the Gemini model based on search results.
        """
        prompt = f"""
        You are a professional researcher. Your task is to generate a comprehensive, well-structured, and easy-to-understand research report in Markdown format.
        **Topic:** {topic}
        Please use the following search results to draft the report. Synthesize the information, identify key findings, and present them in a clear and organized manner. Do not just copy-paste the content.
        **Search Results:** {search_results}
        **Report Structure:**
        1.  **Introduction:** A brief overview of the topic and report scope.
        2.  **Key Findings:** Main points, data, and discoveries from the research. (Use bullet points for clarity).
        3.  **Applications/Examples:** Real-world applications or examples, if applicable.
        4.  **Challenges/Limitations:** Any known challenges, limitations, or controversies.
        5.  **Future Trends:** Potential future developments and trends.
        6.  **Conclusion:** A summary of the key takeaways.
        Begin generating the report now.
        """
        try:
            # The model is now specified directly in the generate_content method. [5]
            response = self.client.models.generate_content(
                model=model_name,
                contents=prompt
            )
            # Accessing the response text remains the same. [5]
            if hasattr(response, 'text'):
                return response.text
            else:
                logging.error("Gemini response did not contain text.")
                return "Error: Failed to generate report due to an unexpected API response."
        except Exception as e:
            logging.error(f"An error occurred while generating the report with Gemini: {e}")
            return f"An error occurred: {e}"