import os
import streamlit as st
from ui.components.editor import detect_language

SUPPORTED_EXTS = [
    'py', 'js', 'ts', 'jsx', 'tsx',
    'java', 'kt', 'cpp', 'c', 'h', 'cs',
    'go', 'rs', 'rb', 'php', 'swift',
    'r', 'pl', 'sh', 'sql', 'lua', 'dart',
]

def render_code_input():
    st.subheader("📂 Code Selection")

    option = st.radio("How to start?", ["Upload file", "Example"], horizontal=True)

    if option == "Upload file":
        uploaded_file = st.file_uploader(
            "Choose file",
            type=SUPPORTED_EXTS
        )
        if uploaded_file:
            st.session_state['code_to_analyze'] = uploaded_file.getvalue().decode("utf-8")
            st.session_state['file_name'] = uploaded_file.name
            st.session_state['lang'] = detect_language(st.session_state['file_name'])
            st.success(f"✅ Ready: {st.session_state['file_name']}")
    else:
        if os.path.exists("examples"):
            example_files = [f for f in os.listdir("examples") if os.path.isfile(os.path.join("examples", f))]
            selected_example = st.selectbox("Select example:", ["-- Select --"] + example_files)
            if selected_example != "-- Select --":
                with open(os.path.join("examples", selected_example), "r", encoding="utf-8") as f:
                    st.session_state['code_to_analyze'] = f.read()
                st.session_state['file_name'] = selected_example
                st.session_state['lang'] = detect_language(st.session_state['file_name'])
        else:
            st.error("⚠️ 'examples' folder not found.")

    if st.session_state.get('code_to_analyze'):
        with st.expander("🔍 View source", expanded=False):
            st.code(st.session_state['code_to_analyze'], language=st.session_state.get('lang', 'python'))
