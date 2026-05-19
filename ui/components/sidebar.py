import subprocess
import streamlit as st

@st.cache_data(ttl=60)
def get_ollama_models():
    """Fetch available Ollama models via CLI."""
    try:
        result = subprocess.run(
            ["ollama", "list"],
            capture_output=True,
            text=True,
            timeout=10
        )
        lines = result.stdout.strip().split("\n")
        models = []
        for line in lines[1:]:  # skip header
            parts = line.split()
            if parts:
                models.append(parts[0])
        return models if models else ["phi3:mini", "llama3.2", "mistral"]
    except (FileNotFoundError, subprocess.TimeoutExpired, subprocess.CalledProcessError):
        return ["phi3:mini", "llama3.2", "mistral"]

def _model_index(models, *preferred):
    """Return index of the first preferred model found in list, or 0."""
    for name in preferred:
        for i, m in enumerate(models):
            if m == name:
                return i
    return 0

def _model_name(models, *preferred):
    """Return the first preferred model found in list, or models[0]."""
    for name in preferred:
        if name in models:
            return name
    return models[0] if models else "phi3:mini"

def render_sidebar():
    """
    Renders the sidebar with expanders and technical info for MX450.
    Includes settings for the Code Optimizer Agent.
    """
    models = get_ollama_models()

    default_model = "phi3:mini"
    seeker_model = "qwen2.5-coder:1.5b"

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
                models,
                index=_model_index(models, default_model),
                key=f"analyst_{expert_mode}",
                disabled=not expert_mode
            )
            
            mod_planner = st.selectbox(
                "Research Planner Agent:", 
                models,
                index=_model_index(models, default_model),
                key=f"planner_{expert_mode}",
                disabled=not expert_mode
            )

            mod_seeker = st.selectbox(
                "Web Seeker (Tools):", 
                models,
                index=_model_index(models, seeker_model, default_model),
                key=f"seeker_{expert_mode}",
                disabled=not expert_mode
            )
            
            mod_writer = st.selectbox(
                "Documenter Agent:", 
                models,
                index=_model_index(models, default_model),
                key=f"writer_{expert_mode}",
                disabled=not expert_mode
            )
            
            mod_optimizer = st.selectbox(
                "Code Optimizer Agent:",
                models,
                index=_model_index(models, default_model),
                key=f"optimizer_{expert_mode}",
                disabled=not expert_mode
            )

        # --- DESPLEGABLE 2: TEMPERATURAS ---
        with st.expander("🌡️ Agent Temperatures", expanded=expert_mode):
            t_analyst   = st.slider("Analyst", 0.0, 1.0, 0.1, key=f"t_analyst_{expert_mode}", disabled=not expert_mode)
            t_planner   = st.slider("Planner", 0.0, 1.0, 0.2, key=f"t_planner_{expert_mode}", disabled=not expert_mode)
            t_seeker    = st.slider("Seeker", 0.0, 1.0, 0.1, key=f"t_seeker_{expert_mode}", disabled=not expert_mode)
            t_writer    = st.slider("Writer", 0.0, 1.0, 0.2, key=f"t_writer_{expert_mode}", disabled=not expert_mode)
            t_optimizer = st.slider("Optimizer", 0.0, 1.0, 0.2, key=f"t_optimizer_{expert_mode}", disabled=not expert_mode)
        
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
        if not expert_mode:
            return (
                _model_name(models, default_model),
                _model_name(models, default_model),
                _model_name(models, seeker_model, default_model),
                _model_name(models, default_model),
                _model_name(models, default_model),
                0.1, 0.2, 0.1, 0.2, 0.2,
                expert_mode
            )
        return (
            mod_analyst, mod_planner, mod_seeker, mod_writer, mod_optimizer,
            t_analyst, t_planner, t_seeker, t_writer, t_optimizer, 
            expert_mode
        )