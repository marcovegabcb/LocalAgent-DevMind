import streamlit as st

def render_status_indicator():
    """
    Renders a dynamic system status indicator based on session state with an inline HTML/CSS spinner.
    """
    is_processing = st.session_state.get('processing', False)

    if is_processing:
        status_text = "SYSTEM WORKING" # Quitamos el engranaje de texto porque ya gira el spinner
        status_color = "#e67e22"  # Naranja
        bg_color = "#fdf2e9"      # Fondo naranja claro
        
        st.markdown(f"""
            <style>
                .status-container {{
                    display: flex;
                    align-items: center;
                    justify-content: center;
                    background-color: {bg_color}; 
                    border-radius: 10px; 
                    padding: 12px; 
                    border: 1px solid {status_color}40; 
                    box-shadow: 0 2px 4px rgba(0,0,0,0.02); 
                    margin-bottom: 10px;
                }}
                .loader {{
                    border: 3px solid #f3f3f3;
                    border-top: 3px solid {status_color};
                    border-radius: 50%;
                    width: 18px;
                    height: 18px;
                    animation: spin 1s linear infinite;
                    margin-right: 12px; /* Espacio exacto entre el círculo y el texto */
                    flex-shrink: 0; /* Evita que el círculo se deforme */
                }}
                @keyframes spin {{
                    0% {{ transform: rotate(0deg); }}
                    100% {{ transform: rotate(360deg); }}
                }}
            </style>
            
            <div class="status-container">
                <div class="loader"></div>
                <span style="font-family: 'Segoe UI', sans-serif; font-weight: bold; 
                             color: {status_color}; font-size: 0.9rem; letter-spacing: 0.5px;
                             line-height: 1;">
                    {status_text}
                </span>
            </div>
        """, unsafe_allow_html=True)
        
    else:
        status_text = "🟢 SYSTEM READY"
        status_color = "#2ecc71"  # Verde
        bg_color = "#e8f8f5"      # Fondo verde claro
        
        st.markdown(f"""
            <div style="background-color: {bg_color}; border-radius: 10px; padding: 12px; 
                        border: 1px solid {status_color}40; text-align: center; 
                        box-shadow: 0 2px 4px rgba(0,0,0,0.02); margin-bottom: 10px;">
                <span style="font-family: 'Segoe UI', sans-serif; font-weight: bold; 
                             color: {status_color}; font-size: 0.9rem; letter-spacing: 0.5px;">
                    {status_text}
                </span>
            </div>
        """, unsafe_allow_html=True)