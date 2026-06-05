from crewai import Task

def create_planner_task(agent, analysis_results, language):
    return Task(
        description=f"""
        LANGUAGE: {language}
        ANALYSIS DATA: {analysis_results}

        Extract the research needs:
        1. Identify only THIRD-PARTY external libraries from the data (not stdlib).
        2. Create 2 or 3 specific search queries for each external dependency.
        3. Queries must target: official documentation, main purpose, and installation command.
        
        IMPORTANT: Standard library modules (java.util.*, java.io.*, os, sys, json, etc.)
        are built-in and do NOT need searches. Ignore them.
        If ALL dependencies are standard library, output exactly "NO_EXTERNAL_DEPS".
        
        STRICT RULE: Do not search. Only output a numbered list of queries or "NO_EXTERNAL_DEPS". No paragraphs.
        """,
        expected_output=f"A list of search queries for the {language} dependencies found.",
        agent=agent
    )