import re
import streamlit as st
from ui.components.ui_agents import render_readme_result

def render_results():
    if 'readme' not in st.session_state:
        return

    render_readme_result(st.session_state['readme'])

    if st.session_state['processing'] and not st.session_state.get('optimization_feedback'):
        st.write("")
        st.info("🔮 **Analyzing code architecture...** The Documenter has finished, but the Code Optimizer is still calculating potential improvements. You can read the README above in the meantime!")

    elif st.session_state.get('optimization_feedback'):
        st.write("")
        st.markdown("""
            <div style="background-color: #f4f6fc;
                        border-left: 5px solid #6c5ce7;
                        border-radius: 8px 8px 0px 0px;
                        padding: 16px 20px;
                        margin-top: 25px;
                        box-shadow: 0 2px 4px rgba(0,0,0,0.02);
                        border-top: 1px solid #e1e4ed;
                        border-right: 1px solid #e1e4ed;">
                <div style="font-family: 'Segoe UI', -apple-system, BlinkMacSystemFont, sans-serif;
                            font-weight: 700;
                            color: #6c5ce7;
                            font-size: 1.05rem;
                            letter-spacing: 0.5px;
                            display: flex;
                            align-items: center;
                            gap: 10px;">
                    💡 Possible Code Optimization & Architecture Feedback
                </div>
            </div>
        """, unsafe_allow_html=True)

        with st.container(border=True):
            st.markdown(st.session_state['optimization_feedback'])


def run_execution_pipeline(
    mod_analyst, mod_planner, mod_seeker, mod_writer, mod_optimizer,
    t_analyst, t_planner, t_seeker, t_writer, t_optimizer,
    update_ui, end_ui
):
    from app.crew import run_documenter_crew, run_optimizer_crew

    if 'readme' not in st.session_state:
        try:
            with st.status("📝 Phase 1: Generating README.md...", expanded=True) as status:
                readme_res = run_documenter_crew(
                    mod_analyst, mod_planner, mod_seeker, mod_writer,
                    t_analyst, t_planner, t_seeker, t_writer,
                    st.session_state['lang'],
                    st.session_state['code_to_analyze'],
                    st.session_state['file_name'],
                    update_ui, end_ui
                )
                st.session_state['readme'] = str(readme_res)
                status.update(label="✅ README Ready!", state="complete", expanded=False)
        except Exception as e:
            st.error(f"⚠️ Error en Fase 1: {e}")
            st.session_state['processing'] = False

        st.rerun()

    elif 'readme' in st.session_state and not st.session_state.get('optimization_feedback'):
        try:
            with st.spinner("🔮 Phase 2: Auditing code architecture and potential bottlenecks..."):
                optimization_res = run_optimizer_crew(
                    mod_optimizer, t_optimizer,
                    st.session_state['lang'],
                    st.session_state['code_to_analyze'],
                    st.session_state['file_name'],
                    update_ui, end_ui
                )
                raw = str(optimization_res)
                clean = re.sub(r'^[ \t]*```', '```', raw, flags=re.MULTILINE)
                st.session_state['optimization_feedback'] = clean
        except Exception as e:
            st.error(f"⚠️ Error en Fase 2: {e}")
        finally:
            st.session_state['processing'] = False
            st.rerun()
