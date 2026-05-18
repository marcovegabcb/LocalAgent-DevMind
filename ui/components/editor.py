import streamlit as st
import os

# Internal function to detect programming language
def detect_language(file_name):
    extensions = {
        '.py': 'python',
        '.js': 'javascript',
        '.ts': 'typescript',
        '.jsx': 'react',
        '.tsx': 'react',
        '.java': 'java',
        '.kt': 'kotlin',
        '.kts': 'kotlin',
        '.cpp': 'cpp',
        '.cxx': 'cpp',
        '.cc': 'cpp',
        '.c': 'c',
        '.h': 'c',
        '.hpp': 'cpp',
        '.cs': 'csharp',
        '.fs': 'fsharp',
        '.go': 'go',
        '.rs': 'rust',
        '.rb': 'ruby',
        '.php': 'php',
        '.swift': 'swift',
        '.m': 'objective-c',
        '.mm': 'objective-c',
        '.scala': 'scala',
        '.zig': 'zig',
        '.lua': 'lua',
        '.r': 'r',
        '.pl': 'perl',
        '.pm': 'perl',
        '.sh': 'bash',
        '.bash': 'bash',
        '.zsh': 'bash',
        '.ps1': 'powershell',
        '.sql': 'sql',
        '.dart': 'dart',
        '.elm': 'elm',
        '.ex': 'elixir',
        '.exs': 'elixir',
        '.erl': 'erlang',
        '.hrl': 'erlang',
        '.clj': 'clojure',
        '.cljs': 'clojure',
        '.jl': 'julia',
        '.cr': 'crystal',
        '.nim': 'nim',
        '.v': 'verilog',
        '.sv': 'systemverilog',
        '.vue': 'vue',
        '.svelte': 'svelte',
    }
    ext = os.path.splitext(file_name)[1].lower()
    return extensions.get(ext, "python")

def render_code_input():
    st.subheader("📝 Code Input")
    uploaded_file = st.file_uploader("Upload your file", type=["py", "java", "js", "cpp", "c", "cs"])
    
    ready_code = ""
    language = "python"
    name = ""

    if uploaded_file is not None:
        name = uploaded_file.name
        language = detect_language(name)
        ready_code = uploaded_file.read().decode("utf-8")
        
        # Save to input_code folder
        if not os.path.exists("input_code"):
            os.makedirs("input_code")
            
        with open(os.path.join("input_code", name), "w", encoding="utf-8") as f:
            f.write(ready_code)
            
        st.success(f"✅ File '{name}' ({language}) uploaded successfully.")
        
        with st.expander(f"View source code ({language})"):
            st.code(ready_code, language=language)
            
    return ready_code, language, name