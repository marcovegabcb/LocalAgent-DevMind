# AI Documenter

Multi-agent system that automatically generates professional **README.md** files and code optimization reports from source code using local LLMs (Ollama).

## Description

AI Documenter orchestrates a crew of specialized AI agents to analyze source code, research dependencies, and produce comprehensive documentation. It runs entirely offline using Ollama-hosted models, making it suitable for private or air-gapped projects.

The system operates in two phases:

1. **Documentation Phase** — Analyzes code structure, researches libraries, and writes a complete README.md
2. **Optimization Phase** — Audits the code for performance issues, bugs, and architectural improvements

## Architecture

```
┌─────────────────────────────────────────────────────┐
│                  Streamlit UI (8501)                 │
│  ┌──────────┐ ┌──────────┐ ┌─────────────────────┐ │
│  │ Sidebar  │ │  Main    │ │ Activity Monitor    │ │
│  │ (Config) │ │ (Editor) │ │ (Agent Logs)        │ │
│  └──────────┘ └──────────┘ └─────────────────────┘ │
│  ┌──────────────────────────────────────────────┐   │
│  │            GPU Monitor (8502)                │   │
│  └──────────────────────────────────────────────┘   │
└──────────────────────┬──────────────────────────────┘
                       │
┌──────────────────────▼──────────────────────────────┐
│                  CrewAI Engine                       │
│  ┌─────────┐ ┌─────────┐ ┌─────────┐ ┌──────────┐ │
│  │ Analyst │ │ Planner │ │ Seeker  │ │  Writer  │ │
│  └─────────┘ └─────────┘ └─────────┘ └──────────┘ │
│  ┌───────────┐                                     │
│  │ Optimizer │                                     │
│  └───────────┘                                     │
└──────────────────────┬──────────────────────────────┘
                       │
              ┌────────▼────────┐
              │  Ollama (LLMs)  │
              │  localhost:11434│
              └─────────────────┘
```

### Agents

| Agent | Role |
|---|---|
| **Analyst** | Extracts technical structure: classes, methods, imports |
| **Planner** | Designs search queries for external dependencies |
| **Seeker** | Performs web searches via DuckDuckGo |
| **Writer** | Composes the README.md in professional format |
| **Optimizer** | Audits code for performance and best practices |

## Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/ai-documenter.git
cd ai-documenter

# Create a virtual environment
python -m venv venv
source venv/bin/activate  # Linux/Mac
# venv\Scripts\activate   # Windows

# Install dependencies
pip install -r requirements.txt

# Ensure Ollama is running with at least one model
# ollama pull phi3:mini
```

### Configuration

Set the Ollama host via environment variable (defaults to `http://localhost:11434`):

```bash
export OLLAMA_HOST=http://localhost:11434
```

## Usage

```bash
# Make the launcher executable
chmod +x start_app.sh

# Launch the full system (GPU Monitor + Dashboard)
./start_app.sh
```

Or run the dashboard directly:

```bash
streamlit run ui/dashboard.py --server.port 8501
```

1. Select a code file (upload or choose an example)
2. Configure agents in the sidebar (Expert Mode unlocks custom models)
3. Click **Start Analysis**
4. Review the generated README and optimization feedback

## Technical Features

- **Offline-first** — Uses local Ollama models; no API keys required
- **Multi-agent pipeline** — Sequential crew with specialized roles
- **GPU monitoring** — Real-time temperature and VRAM tracking
- **Expert mode** — Fine-tune agent selection and temperatures
- **Extensible** — Easy to add new agents or tools

## Requirements

- Python 3.10+
- [Ollama](https://ollama.ai) running locally
- NVIDIA GPU recommended (2GB+ VRAM minimum)

## License

MIT
