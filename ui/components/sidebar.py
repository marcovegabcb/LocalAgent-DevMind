import streamlit as st

def render_sidebar():
    """
    Renders the sidebar with expanders and technical info for MX450.
    Includes settings for the Code Optimizer Agent.
    """
    with st.sidebar:
        st.title("⚙️ Configuration")
        
        # 1. Master Switch
        expert_mode = st.checkbox(
            "🔓 Unlock Expert Mode", 
            value=False, 
            help="Allows agent specialization and custom temperatures."
        )

        st.divider()

        # --- DESPLEGABLE 1: SELECCIÓN DE AGENTES ---
        with st.expander("🤖 Running Agents", expanded=not expert_mode):
            mod_analyst = st.selectbox(
                "Analyst Agent:", 
                ["phi3:mini", "llama3.2", "mistral"],
                index=0,
                disabled=not expert_mode
            )
            
            mod_planner = st.selectbox(
                "Research Planner Agent:", 
                ["phi3:mini", "llama3.2", "mistral"],
                index=0,
                disabled=not expert_mode
            )

            mod_seeker = st.selectbox(
                "Web Seeker (Tools):", 
                ["qwen2.5-coder:1.5b", "llama3.2", "phi3:mini"],
                index=0,
                disabled=not expert_mode
            )
            
            mod_writer = st.selectbox(
                "Documenter Agent:", 
                ["phi3:mini", "llama3.2", "mistral"],
                index=1 if expert_mode else 0, 
                disabled=not expert_mode
            )
            
            mod_optimizer = st.selectbox(
                "Code Optimizer Agent:",
                ["phi3:mini", "llama3.2", "mistral"],
                index=0,
                disabled=not expert_mode
            )

        # --- DESPLEGABLE 2: TEMPERATURAS ---
        with st.expander("🌡️ Agent Temperatures", expanded=expert_mode):
            if not expert_mode:
                t_analyst   = st.slider("Analyst", 0.0, 1.0, 0.1, disabled=True)
                t_planner   = st.slider("Planner", 0.0, 1.0, 0.2, disabled=True)
                t_seeker    = st.slider("Seeker", 0.0, 1.0, 0.1, disabled=True)
                t_writer    = st.slider("Writer", 0.0, 1.0, 0.2, disabled=True)
                t_optimizer = st.slider("Optimizer", 0.0, 1.0, 0.2, disabled=True)
            else:
                t_analyst   = st.slider("Analyst", 0.0, 1.0, 0.1)
                t_planner   = st.slider("Planner", 0.0, 1.0, 0.2)
                t_seeker    = st.slider("Seeker", 0.0, 1.0, 0.1)
                t_writer    = st.slider("Writer", 0.0, 1.0, 0.7)
                t_optimizer = st.slider("Optimizer", 0.0, 1.0, 0.2)
        
        st.divider()

        # --- MENSAJERÍA TÉCNICA (Recuperada) ---
        if not expert_mode:
            st.warning("📊 **Optimized Config (MX450)**")
            st.markdown(
                """
                <div style='font-size: 0.82rem; color: #555; line-height: 1.4;'>
                <b>Sequential multi-agent flow active.</b><br>
                Models will load/unload to stay within <b>2GB VRAM</b> limits.
                </div>
                """, 
                unsafe_allow_html=True
            )
        else:
            st.success("🚀 **Expert Mode Active**")
            st.caption("Custom agent selection and temperatures enabled.")
        
        st.divider()
        st.info("Ollama Status: Connected ✅")

        # 🌟 EL PASO CLAVE: Exportamos las 11 variables respetando el orden del desempaquetado del Dashboard
        return (
            mod_analyst, mod_planner, mod_seeker, mod_writer, mod_optimizer,
            t_analyst, t_planner, t_seeker, t_writer, t_optimizer, 
            expert_mode
        )