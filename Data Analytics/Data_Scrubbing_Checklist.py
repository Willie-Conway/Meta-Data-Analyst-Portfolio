# Data Scrubbing Checklist Script

# Define a checklist for data scrubbing
data_scrubbing_checklist = {
    "1. Removing Duplicates": {
        "Identifying Duplicate Records": "Inspect records for duplicates and verify that they are actually a duplicate record.",
        "Remove Duplicate Records": "Remove the duplicate records from your dataset."
    },
    "2. Formatting Records": {
        "Ensure Consistency": "Check all data follow a consistent format and adjust the format if necessary.",
        "Identify the Data Type": "Make sure the data type is clear and identified."
    },
    "3. Solving for Missing Values": {
        "Identify Missing Values": "Scan your data for any values that may be missing.",
        "Solve for Missing Values": "Replace the missing values with text (e.g., NA) or delete the entire record with the missing value."
    },
    "4. Checking for Wrong Values": {
        "Identify Wrong Values": "Scan your data for any wrong values.",
        "Solve for Wrong Values": "Replace the wrong values with the correct ones if you can or delete the entire record with the wrong values."
    }
}

# Function to display the checklist
def display_scrubbing_checklist(checklist):
    print("Data Scrubbing Checklist:\n")
    for category, items in checklist.items():
        print(f"{category}:")
        for item, question in items.items():
            print(f"  - {item}: {question}")
        print()  # Print a blank line for better readability

# Main function to run the script
def main():
    # Display the data scrubbing checklist
    display_scrubbing_checklist(data_scrubbing_checklist)
    
    # Prompt user to review items interactively
    print("You can review each item and check them off as you go.")
    input("Press Enter when you are ready to exit.")

# Check if the script is run directly
if __name__ == "__main__":
    main()
