from crewai.tools import BaseTool
from langchain_community.tools import DuckDuckGoSearchRun

class TechnicalSearchTool(BaseTool):
    name: str = "technical_web_search"
    description: str = "Search for official technical documentation and library explanations."

    def _run(self, query: str) -> str:
        # Añadimos un pequeño truco: forzamos a que busque documentación
        refined_query = f"{query} official documentation technical"
        search = DuckDuckGoSearchRun()
        result = search.run(refined_query)
        
        # Limitamos el texto para no saturar la memoria de los modelos pequeños
        return result[:2000] 

web_search_tool = TechnicalSearchTool()