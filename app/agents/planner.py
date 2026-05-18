from crewai import Agent, LLM
from app import OLLAMA_HOST

def create_planner_agent(selected_model, language, temp):
    native_llm = LLM(
        model=f"ollama/{selected_model}",
        temperature=temp,
        base_url=OLLAMA_HOST
    )
    return Agent(
        role='Research Planner Agent',
        goal=f'Define specific search queries for {language} libraries.',
        backstory=f"""You are a technical strategist. 
        Your mission is to take the list of libraries found in the {language} code 
        and write clear, optimized search queries to find their documentation.
        You do not search; you only prepare the plan for the Seeker.""",
        llm=native_llm,
        verbose=True,
        allow_delegation=False,
        memory=False
    )