from crewai import Agent, LLM
from app import OLLAMA_HOST

def create_analyst_agent(selected_model, language, temp):
    # Bypass: Pasamos el modelo como string "ollama/nombre"
    # Esto evita que Pydantic valide el objeto ChatOllama complejo
    native_llm = LLM(
        model=f"ollama/{selected_model}",
        temperature=temp,
        base_url=OLLAMA_HOST
    )
    return Agent(
        role='Analyst Agent',
        goal=f'Extract the structural technical data of the {language} code.',
        backstory=f"""You are a high-precision data extractor. 
        Your mission is to identify the skeleton of the code: classes, methods, and imports.
        You do not interpret intent; you only report existence.
        Output must be strictly technical and schematic.""",
        llm=native_llm,
        verbose=True,
        allow_delegation=False,
        memory=False
    )