from crewai import Task

def create_analysis_task(agent, code, language):
    return Task(
        description=f"""
        LANGUAGE: {language} 
        CODE: '{code}'
        
        Extract the following points:
        - PURPOSE: One technical sentence explaining what the code does.
        - COMPONENTS: List of class names and function/method names.
        - FLOW: Sequential steps of execution (1, 2, 3...).
        - DEPENDENCIES: Exact list of imported libraries or headers.
        
        STRICT RULE: Use bullet points. No paragraphs. No opinions.
        """,
        expected_output=f"A schematic technical sheet of the {language} code.",
        agent=agent
    )