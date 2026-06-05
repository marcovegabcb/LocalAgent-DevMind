<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/CrewAI-Framework-ff69b4?style=for-the-badge" alt="CrewAI">
  <img src="https://img.shields.io/badge/Ollama-Local%20LLMs-orange?style=for-the-badge&logo=ollama&logoColor=white" alt="Ollama">
  <img src="https://img.shields.io/badge/Streamlit-UI-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white" alt="Streamlit">
  <img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge" alt="License">
</p>

<h1 align="center">🤖  Multi-Agent AI Documenter & Optimizer</h1>
<p align="center"><em>Transform any source code into professional documentation and optimization audits — fully offline, powered by local LLMs.</em></p>

---

## 🚀 Key Highlights

- **100% Privacy & Offline-First** — Zero external API calls. Your code never leaves your machine.
- **Dual-Phase Execution Engine** — Prevents VRAM overflow and context saturation by isolating heavy agent tasks into two decoupled phases.
- **Hardware-Aware UI** — Real-time GPU temperature, VRAM utilization, and agent activity trackers embedded in the dashboard.
- **Granular Hyperparameter Control** — Adjust independent temperatures per agent (from strict analytical to highly creative prose).

---

## 🔍 Overview

The system analyzes source code and produces two deliverables through an intelligent, sequential pipeline:

| Phase | Output | Agent Crew |
|---|---|---|
| **1. Documentation** | A complete `README.md` with description, installation, usage, and technical features | Analyst → Planner → Seeker → Writer |
| **2. Optimization** | A code audit report with performance bottlenecks, bugs, and actionable fixes | Optimizer (isolated) |

### 🧠 Dual-Phase Workflow

To operate smoothly on consumer-grade hardware (NVIDIA GPUs with 2GB+ VRAM), execution is decoupled into two isolated phases:

1. **Phase 1 — Documentation Crew (Multi-Agent Sequential):** The Analyst, Planner, Seeker, and Writer form a cooperative pipeline. They map code structure, search documentation via DuckDuckGo, and compile a professional README.md.

2. **Phase 2 — Optimization Crew (Isolated Auditing):** Once Phase 1 finishes, its context is released from VRAM, and a single specialized Optimizer agent runs independently. This prevents context blending and eliminates OOM crashes.

---

## 🏗️ System Architecture

<img width="1166" height="925" alt="imagen" src="https://github.com/user-attachments/assets/efe807a1-e1aa-4ce7-943d-ba24a2223a58" />


## 🤖 Agent Crew

| Agent | Model (default) | Temp | Core Responsibility |
|---|---|---|---|
| 🔍 **Analyst** | `phi3:mini` | 0.1 | Extracts architecture, imports, classes, methods, and execution flow |
| 🎯 **Planner** | `phi3:mini` | 0.2 | Deconstructs dependencies into optimized search queries |
| 🌐 **Seeker** | `qwen2.5-coder:1.5b` | 0.1 | Executes DuckDuckGo searches; scrapes documentation and install commands |
| ✍️ **Writer** | `llama3.2` | 0.2 | Synthesizes all inputs into a polished, markdown-compliant README.md |
| 🔮 **Optimizer** | `phi3:mini` | 0.2 | Audits code for performance bottlenecks, memory leaks, and bad practices |

> 💡 **Expert Mode** unlocks full control over model selection and temperature per agent.

---

## ⚡ Quick Start

### Prerequisites

- Python 3.10+
- [Ollama](https://ollama.ai) installed and running
- NVIDIA GPU recommended (2GB+ VRAM minimum)

### Installation

```bash
# Clone
git clone https://github.com/marcovegabcb/LocalAgent-DevMind.git
cd LocalAgent-DevMind

# Virtual environment
python -m venv .venv
source .venv/bin/activate     # Linux/macOS
# .venv\Scripts\activate      # Windows

# Install dependencies
pip install --upgrade pip
pip install -r requirements.txt

# Pull lightweight models (adjust based on your VRAM)
ollama pull phi3:mini
ollama pull llama3.2
ollama pull qwen2.5-coder:1.5b
```

### Configuration

```bash
# Optional: override Ollama host (default: http://localhost:11434)
export OLLAMA_HOST=http://localhost:11434
```

### Run

```bash
# Full system (GPU Monitor + Dashboard)
chmod +x start_app.sh
./start_app.sh

# Or just the dashboard
streamlit run ui/dashboard.py --server.port 8501
```

---

## 📖 Usage Walkthrough

1. **Load Code** — Upload a file or pick an example from the built-in library
2. **Configure** — Toggle **Expert Mode** in the sidebar to assign specific models and temperatures per agent
3. **Analyze** — Click **🚀 Start Analysis**; the Activity Monitor shows real-time agent communication and progress
4. **Export** — Review the generated README and optimization audit; use the built-in download buttons to export instantly

### Example

The system takes raw source code like this `image_downloader.py`:

```python
import requests
from PIL import Image
from io import BytesIO

def download_and_show_image(url):
    response = requests.get(url)
    img = Image.open(BytesIO(response.content))
    print(f"Imagen descargada: {img.size} - {img.mode}")
    return img

img = download_and_show_image("https://via.placeholder.com/150")
print("Tamaño:", img.size)
```

And produces a complete `README.md` with installation instructions, usage examples, and a dependency table — plus an optimization audit identifying potential improvements.

**Generated README:**

> # ImageDownloader
>
> ## Description
>
> This Python script downloads an image from a specified URL and prints its size (width x height) along with the mode of the image to standard output for immediate verification before returning it for further use. It leverages third-party libraries such as `requests` for HTTP requests, `PIL`'s Image module for handling images in memory, and `BytesIO` from Python's standard library for creating an in-memory bytes buffer to hold image data temporarily during the download process.
>
> ## Installation
>
> ```bash
> pip install requests pillow
> ```
>
> ## Usage
>
> ```python
> from image_downloader import download_and_show_image
>
> img = download_and_show_image("https://via.placeholder.com/150")
> print(f"Tamaño: {img.size}")
> ```
>
> ## Technical Features
>
> | Library | Purpose | Installation |
> |---|---|---|
> | `requests` | HTTP request handling | `pip install requests` |
> | `Pillow` | Image processing | `pip install pillow` |
> | `io.BytesIO` | In-memory bytes buffer | Built-in (no install) |

**Generated Optimization:**

> **Suggested improvements:**
>
> - Use context managers to handle HTTP requests and image processing resources.
> - Implement error handling for network issues or unsuccessful downloads.
> - Close the `BytesIO` object after use to optimize memory usage.
>
> **Refactored code:**
>
> ```python
> import requests
> from PIL import Image
> from io import BytesIO
>
> def download_and_show_image(url):
>     try:
>         with requests.get(url, timeout=10) as response:
>             response.raise_for_status()
>             img = Image.open(BytesIO(response.content))
>             print(f"Imagen descargada: {img.size} - {img.mode}")
>             return img
>     except requests.RequestException as e:
>         print(f"Error al descargar la imagen: {e}")
>         return None
> ```

---

## ✨ Features

| Feature | Description |
|---|---|
| **100% Offline** | All LLM inference runs locally via Ollama — zero data leaves your machine |
| **Dual-Phase Pipeline** | Documentation + optimization in a single click, with automatic context isolation |
| **GPU Monitoring** | Live temperature and VRAM tracking embedded in the dashboard |
| **Expert Mode** | Fine-grained control over agent selection and creativity (temperature) |
| **Multi-Language** | Supports Python, JavaScript, TypeScript, Java, C++, Go, Rust, and 30+ more |
| **Extensible** | Plugin-ready agent and tool architecture via CrewAI |

---

## 🧰 Tech Stack

| Component | Technology |
|---|---|
| **Framework** | [CrewAI](https://crewai.com) — Multi-agent orchestration |
| **LLM Gateway** | [Ollama](https://ollama.ai) — Local model serving |
| **UI** | [Streamlit](https://streamlit.io) — Rapid dashboard prototyping |
| **Web Search** | DuckDuckGo (via `langchain-community`) |
| **Language** | Python 3.10+ |

---

## 📁 Project Structure

```
LocalAgent-DevMind/
├── app/
│   ├── agents/          # Agent definitions (Analyst, Planner, Seeker, Writer, Optimizer)
│   ├── tasks/           # Task definitions with strict prompts for each agent
│   ├── tools/           # Custom tools (web search, etc.)
│   └── crew.py          # Dual-phase orchestration (run_documenter_crew, run_optimizer_crew)
├── ui/
│   ├── components/      # Modular Streamlit components (sidebar, monitors, viewers)
│   ├── dashboard.py     # Main application entrypoint
│   └── gpu_live.py      # Standalone GPU monitor (port 8502)
├── examples/            # Sample code files for testing
├── requirements.txt     # Python dependencies
├── start_app.sh         # Launcher script
└── .gitignore
```

---

## 🚀 Roadmap

- [ ] Support for remote LLM providers (OpenAI, Anthropic)
- [ ] Batch processing of entire repositories
- [ ] Custom output templates
- [ ] Multi-language README generation
- [ ] VS Code extension


---

## 📄 License

Distributed under the MIT License. See [LICENSE](LICENSE) for details.
