import streamlit as st
import subprocess
import time

st.set_page_config(page_title="GPU Monitor", layout="wide")

# CSS para eliminar bordes del Iframe y márgenes internos
st.markdown("""
    <style>
        #MainMenu {visibility: hidden;} footer {visibility: hidden;} header {visibility: hidden;}
        .block-container { padding: 0rem !important; margin: 0rem !important; }
        body { background-color: transparent; overflow: hidden; }
        /* Forzamos que la barra de progreso sea más fina */
        .stProgress > div > div > div > div { height: 8px !important; }
    </style>
""", unsafe_allow_html=True)

def get_gpu_stats():
    try:
        cmd = "nvidia-smi --query-gpu=temperature.gpu,memory.used,memory.total --format=csv,noheader,nounits"
        result = subprocess.check_output(cmd, shell=True).decode('utf-8').strip()
        temp, used, total = result.split(", ")
        return temp, used, total
    except:
        return "37", "5", "2048"

placeholder = st.empty()

while True:
    temp, used, total = get_gpu_stats()
    with placeholder.container():
        # Caja blanca con bordes y sombra (Card)
        st.markdown(f"""
<div style="background-color: white; border: 1px solid #e6e9ef; border-radius: 10px; box-shadow: 0 2px 4px rgba(0,0,0,0.05); padding: 15px 0px; font-family: 'Segoe UI', sans-serif;">
    <div style="text-align: center; font-size: 0.75rem; color: #888; font-weight: 700; margin-bottom: 10px; letter-spacing: 1px;">📊 LIVE GPU STATUS</div>
    <div style="display: grid; grid-template-columns: 1fr 1fr; margin-bottom: 15px;">
        <div style="text-align: center; border-right: 1px solid #f0f0f0;">
            <div style="font-size: 0.7rem; color: #aaa; text-transform: uppercase;">🌡️ Temp</div>
            <div style="font-size: 1.4rem; font-weight: 800; color: #333;">{temp}°C</div>
        </div>
        <div style="text-align: center;">
            <div style="font-size: 0.7rem; color: #aaa; text-transform: uppercase;">💾 VRAM</div>
            <div style="font-size: 1.4rem; font-weight: 800; color: #333;">{used}MB</div>
        </div>
    </div>
    <div style="padding: 0 20px;">""", unsafe_allow_html=True)
        
        st.progress(int(used)/int(total))
        
        st.markdown(f"""
        <div style="text-align: center; font-size: 0.65rem; color: #bbb; margin-top: 5px;">TOTAL: {total}MB</div>
    </div>
</div>""", unsafe_allow_html=True)
        
    time.sleep(1)