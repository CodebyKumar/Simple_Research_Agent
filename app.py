import streamlit as st
from utils.agent import ResearchAgent
import os
import shutil

st.title("Research Agent (Gemini)")

with st.expander("Get API Keys"):
    st.markdown("- [Get a Serper API Key](https://serper.dev/) (for Google Search)")
    st.markdown("- [Get a Google Gemini API Key](https://ai.google.dev/) (for report generation)")
    st.info("You can obtain free or trial API keys from the above links. Paste them below to use the app without editing .env files.")

serper_api_key = st.text_input("Enter your Serper API Key", type="password")
gemini_api_key = st.text_input("Enter your Google Gemini API Key", type="password")

topic = st.text_input("Enter a research topic:")

def clean_markdown_output(md: str) -> str:
    md = md.strip()
    for marker in ("```markdown", "```"):
        if md.startswith(marker):
            md = md[len(marker):].lstrip("\n")
    if md.endswith("```"):
        md = md[:-3].rstrip("\n")
    return md

# State for report content and filename
if 'report_content' not in st.session_state:
    st.session_state['report_content'] = None
if 'report_filename' not in st.session_state:
    st.session_state['report_filename'] = None

# UI: Run Research button
if st.button("Run Research"):
    if not (serper_api_key and gemini_api_key):
        st.warning("Please enter both API keys to use the app.")
    elif not topic.strip():
        st.warning("Please enter a topic to research.")
    else:
        agent = ResearchAgent(serper_api_key=serper_api_key, google_api_key=gemini_api_key)
        with st.spinner("Running research with Gemini..."):
            result = agent.run_research(topic)
        cleaned_result = clean_markdown_output(result)
        st.session_state['report_content'] = cleaned_result
        # Find the latest report file in the reports directory
        reports_dir = 'reports'
        files = [f for f in os.listdir(reports_dir) if f.endswith('.md')]
        if files:
            latest_file = max(files, key=lambda x: os.path.getctime(os.path.join(reports_dir, x)))
            st.session_state['report_filename'] = os.path.join(reports_dir, latest_file)

# UI: Show report and download button if report is generated
if st.session_state['report_content']:
    st.markdown("### Research Report")
    st.markdown(st.session_state['report_content'], unsafe_allow_html=False)
    btn = st.download_button(
        label="Download Report as Markdown",
        data=st.session_state['report_content'],
        file_name=os.path.basename(st.session_state.get('report_filename', 'research_report.md')),
        mime="text/markdown"
    )
    if btn:
        reports_dir = 'reports'
        if os.path.exists(reports_dir):
            shutil.rmtree(reports_dir)
        st.session_state['report_content'] = None
        st.session_state['report_filename'] = None
