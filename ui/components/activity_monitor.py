import streamlit as st

def render_activity_monitor():
    """
    Renders the agent activity logs inside a highly-polished, 
    collapsible expander with perfectly aligned and centered cards.
    """
    # 1. Creamos la persiana principal con estilos CSS inyectados para forzar la simetría
    with st.expander("🕵️ Agent Activity History", expanded=True):
        
        st.markdown("""
            <style>
                /* Forzamos a que el interior del expander elimine paddings raros de Streamlit */
                .stExpander div[data-testid="stExpanderDetails"] {
                    padding: 12px 8px 4px 8px !important;
                }
                /* Aseguramos que el contenedor de los bloques de markdown no tenga márgenes locos */
                [data-testid="stMarkdownContainer"] p {
                    margin-bottom: 0px !important;
                }
            </style>
        """, unsafe_allow_html=True)
        
        # 2. Contenedor interno para los mensajes
        container = st.container()
    
    # 3. Función interna para inyectar las tarjetas pulidas en tiempo real
    def update_status(agent_name, message, color="#3498db"):
        with container:
            st.markdown(f"""
                <div style="background: #fdfdfd; 
                            border-left: 4px solid {color}; 
                            padding: 10px 14px; 
                            border-radius: 6px; 
                            margin: 4px auto 8px auto; /* Centrado y espaciado simétrico */
                            width: 96%; /* Deja un pequeño aire elegante a los lados */
                            box-shadow: 0 1px 3px rgba(0,0,0,0.04);
                            border-top: 1px solid #f0f2f6;
                            border-right: 1px solid #f0f2f6;
                            border-bottom: 1px solid #f0f2f6;">
                    <div style="font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; 
                                font-size: 0.75rem; 
                                color: {color}; 
                                font-weight: 700; 
                                letter-spacing: 0.8px;
                                text-transform: uppercase;">
                        {str(agent_name).upper()}
                    </div>
                    <div style="font-family: 'Segoe UI', -apple-system, BlinkMacSystemFont, Roboto, sans-serif; 
                                font-size: 0.85rem; 
                                color: #31333f; 
                                margin-top: 4px;
                                line-height: 1.4;">
                        {message}
                    </div>
                </div>
            """, unsafe_allow_html=True)

    # 4. Callback de finalización de tareas de CrewAI
    def task_end_callback(task_output):
        agent_role = getattr(task_output, 'agent', "Agent")
        update_status(agent_role, "Stage completed successfully.", "#2ecc71")

    return update_status, task_end_callback