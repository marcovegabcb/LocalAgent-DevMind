from crewai import Agent, LLM
from app import OLLAMA_HOST

def create_optimizer_agent(selected_model, language, temp):
    # Bypass: Pasamos el modelo como string "ollama/nombre"
    # Esto evita que Pydantic valide el objeto ChatOllama complejo
    native_llm = LLM(
        model=f"ollama/{selected_model}",
        temperature=temp,
        base_url=OLLAMA_HOST
    )
    
    return Agent(
        role='Code Optimizer Agent',
        goal=f'Analyze the {language} code to identify bottlenecks, bugs, and propose architectural improvements.',
        backstory=f"""You are an expert Senior Software Engineer and Code Auditor.
        Your mission is to perform a rigorous code review of the provided file.
        You look for memory leaks, performance bottlenecks, readability issues, and bad practices.
        You do not write long essays; you provide sharp, actionable feedback with code suggestions.
        Your tone is professional, constructive, and highly technical.""",
        llm=native_llm,
        verbose=True,
        allow_delegation=False,
        memory=False
    )