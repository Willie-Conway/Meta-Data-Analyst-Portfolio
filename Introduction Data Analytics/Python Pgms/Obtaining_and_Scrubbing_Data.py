# Obtaining and Scrubbing Data

# Anna owns a clothing boutique in New York, 
# called BrightThreads. She sells a mix of clothing
# brands and chooses items for her store that she 
# believes her clients will like. She also sells
# online.

# Anna is working on long-term planning for the upcoming 
# year at BrightThreads. Business has been going well, but 
# she would really like to increase sales and potentially 
# open up a second location in a different neighborhood. 
# Next year, Anna would like to increase her total sales by
# 10%. This would be a very good year for Anna and BrightThreads, 
# but it seems doable based on the last few quarters and with some 
# hard work.

# Using this information, answer the questions below regarding 
# the obtain and scrub stages of the OSEMN process. 

# Anna at BrightThreads has begun the process of gathering data 
# to help analyze current sales. She has collected data on recent 
# online sales directly from the online storefront.

# Access this sample Customer Data and click on Use Template in 
# the upper right corner. You will need to be logged into a Google 
# account to use this template. Anna has isolated 4 different segments 
# that each have issues that need to be fixed. You can access each segment 
# in the four sheets in this one spreadsheet.

# Using what you know about data validity, do you think the data 
# Anna has gathered is valid? Why or why not?

# What issue did you identify in segment 1 of the data?

# What issue did you identify in segment 2 of the data?

# What issue did you identify in segment 3 of the data?

# What issue did you identify in segment 4 of the data?


# Import necessary libraries
import pandas as pd

# Step 1: Define the scenario
def scenario_summary():
    scenario = {
        "business_name": "BrightThreads",
        "owner": "Anna",
        "location": "New York",
        "goal": "Increase total sales by 10% next year.",
        "context": (
            "Anna owns a clothing boutique and sells a mix of clothing brands. "
            "She also sells online and aims to potentially open a second location."
        )
    }
    return scenario

# Step 2: Define the SMART goal
def define_smart_goal():
    smart_goal = {
        "Specific": "Increase total sales by 10%.",
        "Measurable": "Use sales data to track percentage increase.",
        "Achievable": "Based on past performance, this goal is realistic.",
        "Relevant": "Supports Anna's intention to grow the business.",
        "Time-bound": "To be achieved within the next fiscal year."
    }
    return smart_goal

# Step 3: Define the Primary KPI
def primary_kpi():
    return "Total Sales Revenue"

# Step 4: Gather relevant data
def relevant_data():
    data_points = [
        "Historical sales data (monthly and quarterly)",
        "Customer demographics (age, location, purchase history)",
        "Inventory turnover rates",
        "Online vs. in-store sales data",
        "Marketing campaign effectiveness (ROI)"
    ]
    return data_points

# Step 5: Define data acquisition methods
def data_acquisition_methods():
    first_party_data = [
        "Sales records from the point-of-sale (POS) system",
        "Customer data from the e-commerce platform",
        "Customer feedback collected through surveys"
    ]
    third_party_data = [
        "Market research reports on clothing industry trends",
        "Public competitor analysis data"
    ]
    methods = [
        "Web analytics tools (e.g., Google Analytics)",
        "Surveys distributed via email or in-store",
        "Social media analytics for customer engagement"
    ]
    return first_party_data, third_party_data, methods

# Step 6: Analyze data validity
def data_validity_analysis():
    validity_assessment = (
        "The data is not fully valid due to missing values and potential duplicates. "
        "These issues can lead to incorrect conclusions."
    )
    return validity_assessment

# Step 7: Identify issues in the dataset
def identify_data_issues():
    issues = {
        "Segment 1": "Duplicate entries for certain orders (e.g., Dresses entry for customer_id 102537).",
        "Segment 2": "Missing values in several rows, indicating incomplete records.",
        "Segment 3": "Inconsistent formatting in customer_zip, complicating geographic analyses.",
        "Segment 4": "Lacks quantity information per order, limiting sales volume analysis."
    }
    return issues

# Main function to execute the script
def main():
    # Scenario summary
    print("Scenario Summary:")
    print(scenario_summary())

    # SMART goal
    print("\nSMART Goal:")
    print(define_smart_goal())

    # Primary KPI
    print("\nPrimary KPI:")
    print(primary_kpi())

    # Relevant data to gather
    print("\nRelevant Data:")
    print(relevant_data())

    # Data acquisition methods
    first_party, third_party, methods = data_acquisition_methods()
    print("\nFirst-party Data Sources:")
    print(first_party)
    print("\nThird-party Data Sources:")
    print(third_party)
    print("\nData Acquisition Methods:")
    print(methods)

    # Data validity analysis
    print("\nData Validity Assessment:")
    print(data_validity_analysis())

    # Identify issues in the dataset
    print("\nIdentified Data Issues:")
    issues = identify_data_issues()
    for segment, issue in issues.items():
        print(f"{segment}: {issue}")

# Execute the main function
if __name__ == "__main__":
    main()
