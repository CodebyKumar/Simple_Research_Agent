import streamlit as st
from utils.agent import ResearchAgent
import re

st.title("Research Agent")

topic = st.text_input("Enter a research topic:")

def clean_markdown_output(md: str) -> str:
    # Remove leading/trailing code block markers if present
    md = md.strip()
    for marker in ("```markdown", "```"):
        if md.startswith(marker):
            md = md[len(marker):].lstrip("\n")
    if md.endswith("```"):
        md = md[:-3].rstrip("\n")
    return md

if st.button("Run Research"):
    if topic.strip():
        agent = ResearchAgent()
        with st.spinner("Running research with Gemini..."):
            result = agent.run_research(topic)
        cleaned_result = clean_markdown_output(result)
        st.markdown("### Research Report")
        st.markdown(cleaned_result, unsafe_allow_html=False)
    else:
        st.warning("Please enter a topic to research.")
