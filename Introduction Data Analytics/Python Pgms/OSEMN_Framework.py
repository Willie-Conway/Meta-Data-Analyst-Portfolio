# ose_framework.py

"""
OSEMN Framework Overview
This script outlines the OSEMN framework stages: Obtain, Scrub, Explore, Model, and iNterpret.
"""

# Obtain Overview
def obtain_overview():
    """
    Obtain: Gather the data.
    - Determine what data would be useful.
    - Evaluate what data is available.
    - Decide on how the data can be gathered.
    """
    return {
        "stage": "Obtain",
        "description": "Gather the data.",
        "tasks": [
            "Determine what data would be useful.",
            "Evaluate what data is available.",
            "Decide on how the data can be gathered."
        ]
    }

# Scrub Overview
def scrub_overview():
    """
    Scrub: Clean the data to prepare it for analysis.
    - Correct inconsistent formatting.
    - Remove duplicate records.
    - Handle missing values.
    - Remove inaccurate information.
    """
    return {
        "stage": "Scrub",
        "description": "Clean the data to prepare it for analysis.",
        "tasks": [
            "Correct inconsistent formatting.",
            "Remove duplicate records.",
            "Handle missing values.",
            "Remove inaccurate information."
        ]
    }

# Explore Overview
def explore_overview():
    """
    Explore: Search for interesting patterns and statistics that stand out.
    - Examine variable distributions.
    - Examine variable relationships.
    - Perform statistical tests.
    """
    return {
        "stage": "Explore",
        "description": "Search for interesting patterns and statistics that stand out.",
        "tasks": [
            "Examine variable distributions.",
            "Examine variable relationships.",
            "Perform statistical tests."
        ]
    }

# Model Overview
def model_overview():
    """
    Model: Generate predictions and insights.
    - Select a model type for your goals (often in cooperation with a partner).
    - Categories of models include:
        - Classification: Is this “A” or “B”?
        - Regression: How much or how many?
        - Clustering: What natural segments can we find in our data?
    """
    return {
        "stage": "Model",
        "description": "Generate predictions and insights.",
        "tasks": [
            "Select a model type for your goals (often in cooperation with a partner).",
            "Categories of models include:",
            "  - Classification: Is this 'A' or 'B'?",
            "  - Regression: How much or how many?",
            "  - Clustering: What natural segments can we find in our data?"
        ]
    }

# iNterpret Overview
def interpret_overview():
    """
    iNterpret: Help others to understand the results of your analysis.
    - Build visualizations.
    - Construct stories.
    - Create presentations of your findings.
    """
    return {
        "stage": "iNterpret",
        "description": "Help others to understand the results of your analysis.",
        "tasks": [
            "Build visualizations.",
            "Construct stories.",
            "Create presentations of your findings."
        ]
    }

if __name__ == "__main__":
    # Entry point for executing OSEMN framework functions
    stages = [obtain_overview(), scrub_overview(), explore_overview(), model_overview(), interpret_overview()]
    
    for stage in stages:
        print(f"Stage: {stage['stage']}")
        print(f"Description: {stage['description']}")
        print("Tasks:")
        for task in stage["tasks"]:
            print(f" - {task}")
        print()  # Adding a newline for better readability
