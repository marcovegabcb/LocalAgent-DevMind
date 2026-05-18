#!/bin/bash

echo "🚀 Starting AI Documenter Infrastructure..."

# 1. Iniciar Monitor de GPU (Puerto 8502) - Headless para que no abra pestañas locas
streamlit run ui/gpu_live.py --server.port 8502 --server.headless true &
GPU_PID=$!
echo "✅ GPU Monitor running on port 8502 (PID: $GPU_PID)"

# 2. Iniciar Dashboard Principal (Puerto 8501)
echo " principal Dashboard on port 8501..."
streamlit run ui/dashboard.py --server.port 8501

# Al cerrar el dashboard, matamos los procesos secundarios para no dejar basura
trap "kill $GPU_PID" EXIT
