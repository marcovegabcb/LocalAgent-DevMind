import streamlit as st

def render_agents_status(file_name, language):
    """Visual feedback of the agent workflow."""
    with st.status(f"Processing {file_name}...", expanded=True) as status:
        st.write(f"🕵️ Analyzing {language} logic...")
        st.write("🔍 Searching for info on the web...")
        st.write("✍️ Drafting README...")
        status.update(label="✅ Completed!", state="complete", expanded=False)

def render_readme_result(content):
    """Displays the final Markdown and download option."""
    if content:
        st.markdown("---")
        st.markdown("### 📄 Result: README.md")
        st.markdown(content)
        st.download_button(
            label="📥 Download README.md", 
            data=content, 
            file_name="README.md",
            mime="text/markdown"
        )