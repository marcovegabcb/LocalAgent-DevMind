from crewai import Task

def create_writing_task(agent, combined_data, language):
    return Task(
        description=f"""
        Project Context ({language}):
        {combined_data}
        
        Using the data above, generate a professional README.md. 
        
        INSTRUCTIONS:
        1. Name the project based on the main class or file name detected.
        2. Be technically accurate: Only use the methods and logic described in the input.
        3. Clean Output: Ensure no meta-talk, agent names, or internal thoughts appear in the document.
        
        STRUCTURE:
        # [Project Name]
        ## Description
        ## Installation
        ## Usage (Code snippet using the detected class/methods)
        ## Technical Features (Table or List)
        """,
        expected_output="A professional README.md file in English, ready for GitHub.",
        agent=agent
    )