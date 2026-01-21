# Data Exploration Checklist Script

# Define a checklist for data exploration
data_exploration_checklist = {
    "Inspecting Data": {
        "Inspect Your Data": "If your dataset isn’t too large, read through your data to assess whether interesting information jumps out.",
        "Use Summary Statistics": "Evaluate your data by summarizing it (categorize, use statistics like average, standard deviation, etc.).",
        "Inspect a Random Sample": "If your dataset is too large, a random sample may give you some initial information."
    },
    "Visualizing Data": {
        "Visualize Your Data": "Use bar charts, line charts, or scatter plots to examine information hidden in your dataset."
    },
    "Examine Variable Distributions": {
        "Inspect the Distribution": "Inspect the distribution of your data.",
        "Categorize the Data": "Categorize the data and plot the categorized data.",
        "Common Data Distributions": "Normal, Bimodal, Log-normal, Exponential, Uniform."
    },
    "Learn More About Your Data": {
        "Evaluate Minimum": "Evaluate the minimum value of your dataset.",
        "Evaluate Maximum": "Evaluate the maximum value of your dataset.",
        "Evaluate Mode": "Evaluate the mode of your dataset.",
        "Evaluate Standard Deviation": "Evaluate the standard deviation of your dataset."
    },
    "Examine Variable Relationships": {
        "Visualize Variables": "Visualize variables to understand their correlation.",
        "Common Visualizations": "Scatter plot, Line chart.",
        "Calculate Correlation Coefficient": "Understand the strength of the correlation: 0 = no correlation, 1 = perfect positive correlation, -1 = perfect negative correlation."
    },
    "Feature Engineering": {
        "Evaluate New Features": "Evaluate whether we can create new features or modify existing ones to better understand our data."
    }
}

# Function to display the checklist
def display_exploration_checklist(checklist):
    print("Data Exploration Checklist:\n")
    for category, items in checklist.items():
        print(f"{category}:")
        for item, question in items.items():
            print(f"  - {item}: {question}")
        print()  # Print a blank line for better readability

# Main function to run the script
def main():
    # Display the data exploration checklist
    display_exploration_checklist(data_exploration_checklist)
    
    # Prompt user to review items interactively
    print("You can review each item and check them off as you go.")
    input("Press Enter when you are ready to exit.")

# Check if the script is run directly
if __name__ == "__main__":
    main()
