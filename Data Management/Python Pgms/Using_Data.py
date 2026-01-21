# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression


print("All imports successful!")
# Function for data analysis
def data_analysis(data):
    """
    Analyzes past data to find patterns.
    
    Parameters:
        data (DataFrame): A pandas DataFrame containing historical data.
    
    Returns:
        patterns (DataFrame): Identified patterns from the data.
    """
    # Example: Identify correlation between temperature and bathing suit sales
    patterns = data.corr()  # Compute pairwise correlation of columns
    return patterns

# Function for data analytics
def data_analytics(data, patterns):
    """
    Uses insights from data analysis to inform decisions.
    
    Parameters:
        data (DataFrame): A pandas DataFrame containing data.
        patterns (DataFrame): Patterns identified from the data analysis.
        
    Returns:
        recommendations (dict): Recommended actions based on analysis.
    """
    recommendations = {}
    if patterns['temperature']['bathing_suit_sales'] > 0.5:  # Example threshold
        recommendations['bathing_suits'] = 'Increase production during warmer months'
    else:
        recommendations['bathing_suits'] = 'Reduce production'
    return recommendations

# Function for Exploratory Data Analysis (EDA)
def exploratory_data_analysis(data):
    """
    Conducts EDA to gain insights and formulate hypotheses.
    
    Parameters:
        data (DataFrame): A pandas DataFrame containing the data.
    """
    # Summary statistics
    print(data.describe())
    
    # Visualizations
    plt.figure(figsize=(10, 5))
    sns.histplot(data['bathing_suit_sales'], bins=30)
    plt.title('Distribution of Bathing Suit Sales')
    plt.show()

    # Correlation heatmap
    plt.figure(figsize=(10, 8))
    sns.heatmap(data.corr(), annot=True, fmt=".2f", cmap='coolwarm')
    plt.title('Correlation Heatmap')
    plt.show()

# Function for statistical analysis
def statistical_analysis(data):
    """
    Examines and interprets a sample of data.
    
    Parameters:
        data (DataFrame): A pandas DataFrame containing the data.
    
    Returns:
        insights (dict): Quantitative insights and correlations.
    """
    insights = {
        'mean_sales': data['bathing_suit_sales'].mean(),
        'correlation_temp_sales': data['temperature'].corr(data['bathing_suit_sales']),
    }
    return insights

# Function for hypothesis testing
def hypothesis_testing(data):
    """
    Tests hypotheses about a population based on sample data.
    
    Parameters:
        data (DataFrame): A pandas DataFrame containing the data.
    
    Returns:
        results (dict): Results of hypothesis tests.
    """
    # Example: Null hypothesis is that there's no correlation between temperature and sales
    correlation = data['temperature'].corr(data['bathing_suit_sales'])
    results = {
        'correlation': correlation,
        'reject_null': abs(correlation) > 0.3  # Example threshold for significance
    }
    return results

# Function for machine learning model
def machine_learning_model(data):
    """
    Builds a simple machine learning model for predictions.
    
    Parameters:
        data (DataFrame): A pandas DataFrame containing the data.
    
    Returns:
        model (object): Trained machine learning model.
    """
    from sklearn.model_selection import train_test_split
    from sklearn.linear_model import LinearRegression
    
    # Preparing data for training
    X = data[['temperature']]  # Features
    y = data['bathing_suit_sales']  # Target variable
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Creating and training the model
    model = LinearRegression()
    model.fit(X_train, y_train)
    
    # Evaluate model performance
    score = model.score(X_test, y_test)
    print(f'Model R^2 Score: {score}')
    
    return model

# Example usage
if __name__ == "__main__":
    # Sample data creation
    data = pd.DataFrame({
        'temperature': [70, 75, 80, 85, 90, 95, 100],
        'bathing_suit_sales': [5, 10, 15, 20, 25, 30, 35]
    })
    
    # Perform analysis and modeling
    patterns = data_analysis(data)
    recommendations = data_analytics(data, patterns)
    print("Recommendations:", recommendations)
    
    exploratory_data_analysis(data)
    
    insights = statistical_analysis(data)
    print("Statistical Insights:", insights)
    
    testing_results = hypothesis_testing(data)
    print("Hypothesis Testing Results:", testing_results)
    
    model = machine_learning_model(data)
