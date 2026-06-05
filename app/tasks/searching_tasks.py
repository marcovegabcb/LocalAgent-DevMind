from crewai import Task

def create_seeker_task(agent, planner_output, language):
    return Task(
        description=f"""
        LANGUAGE: {language}
        SEARCH QUERIES: 
        {planner_output}

        Execution instructions:
        1. If the input says "NO_EXTERNAL_DEPS", just output "No external dependencies found." and skip searching.
        2. Otherwise, use the 'technical_web_search' tool for EVERY query provided.
        3. For each library, extract: Short description and official installation command.
        4. If no info is found, mark it as 'Not found in official sources'.
        
        STRICT RULE: You MUST use the tool if there are queries. Do not answer from memory. No meta-talk.
        """,
        expected_output=f"Technical data and installation steps for each {language} library.",
        agent=agent,
        context=[planner_output]
    )