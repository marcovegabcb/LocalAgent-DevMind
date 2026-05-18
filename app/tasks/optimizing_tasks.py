from crewai import Task

def create_optimization_task(agent, code, language):
    return Task(
        description=f"""
        LANGUAGE: {language}
        CODE: '{code}'
        
        Extract the following optimization points:
        - IMPROVEMENTS: List 2 or 3 critical technical improvements (performance, memory, or best practices).
        - REASON: One single sentence explaining why each improvement is needed.
        - SOLUTION: A minimalist code snippet or fix for each point.
        
        STRICT RULE: Use bullet points. No introductory text. No conversational prose. No opinions.
        """,
        expected_output=f"A schematic list of technical improvements for the {language} code.",
        agent=agent
    )