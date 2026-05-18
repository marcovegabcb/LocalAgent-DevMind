# app/agents/seeker.py

from crewai import Agent, LLM
from app import OLLAMA_HOST
from app.tools.web_tools import web_search_tool

def create_seeker_agent(selected_model, language, temp): 
    native_llm = LLM(
        model=f"ollama/{selected_model}",
        temperature=temp, 
        base_url=OLLAMA_HOST
    )
    return Agent(
        role='Web Seeker Agent',
        goal=f'Execute web searches to find technical info about {language} libraries.',
        backstory="""You are a precise search robot. 
        You take queries and MUST use the 'technical_web_search' tool.
        You provide the raw results from the web (purpose and installation).
        Do not explain; just search and report.""",
        llm=native_llm,
        tools=[web_search_tool],
        verbose=True,
        allow_delegation=False,
        memory=False,
        max_iter=5
    )