import sys
import os
import streamlit as st

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
st.set_page_config(page_title="AI Documenter", layout="wide", page_icon="🤖")

from ui.components.sidebar import render_sidebar
from ui.components.gpu_monitor import render_gpu_monitor
from ui.components.status_indicator import render_status_indicator
from ui.components.activity_monitor import render_activity_monitor
from ui.components.code_input import render_code_input
from ui.components.results_viewer import render_results, run_execution_pipeline

st.markdown("""
    <style>
        button[disabled] { opacity: 0.6 !important; cursor: not-allowed !important; }
        .block-container { padding-top: 2rem; padding-bottom: 2rem; }
        .stMarkdown pre, code { white-space: pre-wrap !important; word-break: break-all !important; }
    </style>
""", unsafe_allow_html=True)

for key, default in [('processing', False), ('code_to_analyze', ""),
                     ('file_name', ""), ('lang', "python"),
                     ('optimization_feedback', "")]:
    if key not in st.session_state:
        st.session_state[key] = default

(mod_analyst, mod_planner, mod_seeker, mod_writer, mod_optimizer,
 t_analyst, t_planner, t_seeker, t_writer, t_optimizer,
 expert_mode) = render_sidebar()

st.title("🤖 Multi-Agent AI Documenter & Optimizer")
st.caption("Advanced dual-phase architecture for automated documentation and code auditing powered by local LLMs.")

col_left, col_right = st.columns([3, 1])

with col_right:
    render_gpu_monitor()
    render_status_indicator()
    st.divider()
    update_ui, end_ui = render_activity_monitor()

with col_left:
    render_code_input()

    st.divider()

    if st.session_state['processing']:
        btn_label = "⏳ Running Intelligence Pipeline..."
        is_disabled = True
    else:
        btn_label = "🚀 Start Analysis"
        is_disabled = False

    if st.button(btn_label, use_container_width=True, disabled=is_disabled):
        if st.session_state['code_to_analyze']:
            st.session_state['processing'] = True
            for key in ['readme', 'final_result']:
                if key in st.session_state:
                    del st.session_state[key]
            st.session_state['optimization_feedback'] = ""
            st.rerun()
        else:
            st.error("❌ Please select code first.")

    st.divider()

    render_results()

    if st.session_state['processing']:
        run_execution_pipeline(
            mod_analyst, mod_planner, mod_seeker, mod_writer, mod_optimizer,
            t_analyst, t_planner, t_seeker, t_writer, t_optimizer,
            update_ui, end_ui
        )
