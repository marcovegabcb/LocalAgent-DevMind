<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://img.shields.io/badge/python-3.10+-blue?logo=python&logoColor=white">
    <img alt="Python" src="https://img.shields.io/badge/python-3.10+-blue?logo=python&logoColor=white">
  </picture>
  <img src="https://img.shields.io/badge/license-MIT-green">
  <img src="https://img.shields.io/badge/ollama-required-orange?logo=ollama">
  <img src="https://img.shields.io/badge/streamlit-3.0-red?logo=streamlit">
  <img src="https://img.shields.io/badge/crewai-powered-6c5ce7">
</p>

<h1 align="center">🤖 Multi-Agent AI Documenter & Optimizer</h1>
<p align="center"><em>Transform any source code into professional documentation — fully offline, powered by local LLMs.</em></p>

---

## 🔍 Overview

AI Documenter is a **dual-phase autonomous system** that analyzes source code and produces two deliverables:

| Phase | Output | Agent Crew |
|---|---|---|
| **1. Documentation** | A complete `README.md` with description, installation, usage, and technical features | Analyst → Planner → Seeker → Writer |
| **2. Optimization** | A code audit report with performance bottlenecks, bugs, and actionable fixes | Optimizer |

It runs **100% offline** using Ollama-hosted models — no API keys, no internet dependency once models are pulled.

---

## 🏗️ Architecture

```
┌──────────────────────────────────────────────────────────┐
│                    Streamlit UI (8501)                    │
│  ┌────────────┐  ┌──────────────┐  ┌──────────────────┐ │
│  │   Sidebar  │  │  Main Panel  │  │ Activity Log     │ │
│  │  (Config)  │  │  (Editor)    │  │ (Live Agent Tx)  │ │
│  └────────────┘  └──────────────┘  └──────────────────┘ │
│  ┌──────────────────────────────────────────────────────┐ │
│  │              GPU Live Monitor (8502)                  │ │
│  └──────────────────────────────────────────────────────┘ │
└──────────────────────┬───────────────────────────────────┘
                       │
┌──────────────────────▼───────────────────────────────────┐
│                    CrewAI Engine                          │
│                                                          │
│  ┌──────────┐  ┌──────────┐  ┌────────┐  ┌──────────┐  │
│  │ Analyst  │→ │ Planner  │→ │ Seeker │→ │  Writer  │  │
│  └──────────┘  └──────────┘  └────────┘  └──────────┘  │
│                                                          │
│  ┌────────────┐                                          │
│  │ Optimizer  │  (Phase 2, runs independently)           │
│  └────────────┘                                          │
└──────────────────────┬───────────────────────────────────┘
                       │
              ┌────────▼────────┐
              │   Ollama API    │
              │  localhost:11434│
              └─────────────────┘
```

---

## 🤖 Agent Crew

Each agent has a single responsibility and uses a configurable local LLM:

| Agent | Model (default) | Temperature | Responsibility |
|---|---|---|---|
| **Analyst** | `phi3:mini` | 0.1 | Extracts classes, methods, imports, and execution flow |
| **Planner** | `phi3:mini` | 0.2 | Generates targeted search queries for external dependencies |
| **Seeker** | `qwen2.5-coder:1.5b` | 0.1 | Executes DuckDuckGo searches for documentation & install commands |
| **Writer** | `llama3.2` | 0.2 | Composes a polished README.md following a strict template |
| **Optimizer** | `phi3:mini` | 0.2 | Audits code for performance, security, and maintainability issues |

> 💡 **Expert Mode** unlocks full control over model selection and temperature per agent.

---

## ⚡ Quick Start

### Prerequisites

- Python 3.10+
- [Ollama](https://ollama.ai) installed and running
- At least one model pulled (recommended: `phi3:mini`, `llama3.2`, `qwen2.5-coder:1.5b`)

### Installation

```bash
# Clone
git clone https://github.com/marcovegabcb/LocalAgent-DevMind.git
cd LocalAgent-DevMind

# Virtual environment
python -m venv venv
source venv/bin/activate   # Linux/macOS

# Dependencies
pip install -r requirements.txt

# Pull models (adjust based on your VRAM)
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

1. **Select code** — Upload a file or pick an example from the built-in library
2. **Configure** — Toggle Expert Mode in the sidebar to customize agents
3. **Analyze** — Click *Start Analysis*; the activity monitor shows real-time agent communication
4. **Review** — The generated README appears instantly; optimization feedback follows shortly after

### Example Output

The system takes raw source code like this `web_scraper.py`:

```python
import requests
from bs4 import BeautifulSoup

def fetch_top_stories(url):
    response = requests.get(url, timeout=5)
    soup = BeautifulSoup(response.text, 'html.parser')
    headlines = [h.get_text() for h in soup.find_all('h2')[:5]]
    return headlines
```

And produces a complete `README.md` with installation instructions, usage examples, and a dependency table.

---

## ✨ Features

| Feature | Description |
|---|---|
| **Offline-first** | All LLM inference runs locally via Ollama — zero data leaves your machine |
| **Sequential pipeline** | Agents pass context forward, preventing VRAM overload on consumer GPUs |
| **GPU monitoring** | Live temperature and VRAM tracking embedded in the dashboard |
| **Dual-phase** | Documentation + optimization in a single click |
| **Expert Mode** | Fine-grained control over agent selection and creativity (temperature) |
| **Multi-language** | Supports Python, JavaScript, TypeScript, Java, C++, Go, Rust, and 30+ more |
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
│   ├── tasks/           # Task definitions with prompts for each agent
│   ├── tools/           # Custom tools (web search, etc.)
│   └── crew.py          # Crew orchestration (Phase 1 & Phase 2)
├── ui/
│   ├── components/      # Streamlit UI components
│   ├── dashboard.py     # Main application entrypoint
│   └── gpu_live.py      # Standalone GPU monitor
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

## 🤝 Contributing

Contributions are welcome! Feel free to open issues or submit pull requests.

---

## 📄 License

MIT — see [LICENSE](LICENSE) for details.
