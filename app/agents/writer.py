from crewai import LLM, Agent
from app import OLLAMA_HOST

def create_writer_agent(selected_model, language, temp):
    # Bypass: Formato string para evitar el ValidationError
    native_llm = LLM(
        model=f"ollama/{selected_model}",
        temperature=temp,
        base_url=OLLAMA_HOST
    )

    return Agent(
        role='Documenter Agent',
        goal='Generate a comprehensive and clean README.md based on provided technical analysis.',
        backstory=f"""You are an expert Technical Writer specialized in {language} projects.
        Your mission is to transform raw technical data into a professional README.md.
        
        GUIDELINES:
        - Structure: Use # Title, ## Description, ## Installation, ## Usage, and ## Technical Features.
        - Consistency: Use the EXACT class and function names provided by the Analyst.
        - Content: Be thorough but relevant. If the project is small, be concise; if it is complex, provide detail.
        - Cleanliness: Filter out any metadata, agent conversation traces, or "hypothetical" remarks.
        - Tone: Professional, objective, and developer-oriented.""",
        llm=native_llm,
        verbose=True,
        allow_delegation=False,
        use_system_prompt=True,
        respect_context_window=True
    )