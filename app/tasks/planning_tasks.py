from crewai import Task

def create_planner_task(agent, analysis_results, language):
    return Task(
        description=f"""
        LANGUAGE: {language}
        ANALYSIS DATA: {analysis_results}

        Extract the research needs:
        1. Identify the external libraries and modules from the data.
        2. Create 2 or 3 specific search queries for each external dependency.
        3. Queries must target: official documentation, main purpose, and installation command.
        
        STRICT RULE: Do not search. Only output a numbered list of queries. No paragraphs.
        """,
        expected_output=f"A list of search queries for the {language} dependencies found.",
        agent=agent
    )