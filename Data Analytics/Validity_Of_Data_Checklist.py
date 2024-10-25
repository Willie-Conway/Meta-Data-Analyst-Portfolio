# Validity of Data Checklist Script

# Define a checklist for data validity
data_validity_checklist = {
    "Source Credibility": {
        "Authorship": "Is the data provided by a reputable author or organization? What are the credentials of the author or organization?",
        "Publication Date": "Is the data current and up-to-date?"
    },
    "Methodology": {
        "Sample Size": "Was the data collected from a large enough sample?",
        "Sampling Method": "Was the sampling method unbiased and representative?",
        "Data Collection": "Were the data collection methods clearly described and appropriate?"
    },
    "Objectivity": {
        "Bias": "Are there any apparent biases in the data or its presentation?",
        "Conflicts of Interest": "Are there any potential conflicts of interest that could influence the data?"
    },
    "Accuracy": {
        "Consistency": "Are the data consistent with other reputable sources?",
        "Error Rate": "Are there any obvious errors or inconsistencies in the data?"
    },
    "Relevance": {
        "Scope": "Is the data relevant to the research question or topic?",
        "Context": "Is the data presented within a meaningful context?"
    }
}

# Function to display the checklist
def display_checklist(checklist):
    print("Data Validity Checklist:\n")
    for category, items in checklist.items():
        print(f"{category}:")
        for item, question in items.items():
            print(f"  - {item}: {question}")
        print()  # Print a blank line for better readability

# Main function to run the script
def main():
    # Display the validity checklist
    display_checklist(data_validity_checklist)
    
    # Prompt user to check off items interactively
    print("You can review each item and check them off as you go.")
    input("Press Enter when you are ready to exit.")

# Check if the script is run directly
if __name__ == "__main__":
    main()
