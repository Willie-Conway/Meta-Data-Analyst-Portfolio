# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Understand the results of your analysis

def analyze_data(data):
    # Objective for the analysis
    objective = "Understand the sales performance over the last quarter."
    
    # Data analysis (example)
    total_sales = data['Sales'].sum()
    avg_sales = data['Sales'].mean()
    
    # Answering the questions
    analysis_questions = {
        "Objective": objective,
        "Total Sales": total_sales,
        "Average Sales": avg_sales,
        "Learnings": "Sales increased in the last month due to a marketing campaign.",
        "Business Application": "Consider running similar campaigns in the future.",
        "Confidence Level": "High",
        "Model Accuracy": "Model predicts sales with 90% accuracy.",
        "Potential Errors": "Fluctuations in market demand can affect predictions."
    }
    
    return analysis_questions

# Step 2: Explain your findings

def create_presentation(analysis_questions):
    # Recap
    print("Recap: Sales performance analysis for the last quarter.")
    
    # Method
    print("\nMethod: Analyzed sales data using pandas for aggregation.")
    
    # Visualization
    plt.figure(figsize=(10, 5))
    plt.plot(data['Date'], data['Sales'], marker='o')
    plt.title('Sales Performance Over Last Quarter')
    plt.xlabel('Date')
    plt.ylabel('Sales')
    plt.xticks(rotation=45)
    plt.grid()
    plt.show()
    
    # Explanation
    print("\nExplanation: The data shows a clear upward trend in sales over the last quarter.")
    
    # Recommendation
    print("\nRecommendation: Continue with marketing efforts that have shown to increase sales.")

# Sample data (you would replace this with actual data)
data = pd.DataFrame({
    'Date': pd.date_range(start='2023-07-01', periods=90, freq='D'),
    'Sales': [x + (x * 0.05 * (x % 30)) for x in range(90)]  # Simulated sales data
})

# Running the analysis and presentation
analysis_results = analyze_data(data)
create_presentation(analysis_results)
