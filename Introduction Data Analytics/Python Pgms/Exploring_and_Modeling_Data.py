# Exporing and Modeling Data

# In this activity, we explore and model the online sales data from Anna's clothing boutique, BrightThreads.
# We follow the OSEMN process (Obtain, Scrub, Explore, Model, and Interpret) to analyze the dataset,
# create visualizations, and develop a linear regression model to predict site visits based on social media ad spend.
# This exercise helps to gain insights into customer behavior and the effectiveness of marketing strategies.

# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Sample Data: BrightThreads Online Sales Data
sales_data = {
    "sale_date": ["01/01", "01/03", "01/05", "01/07", "01/09", "01/11", "01/13", "01/15", "01/17"],
    "order_total": [65.99, 129.99, 65.99, 89.99, 65.99, 149.99, 49.99, 139.99, 109.99],
    # Additional data...
}

# Sample Data: Q1 Weekly Ad Spend and Visits
ad_data = {
    "week_num": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
    "social_ad_spend": [100, 75, 100, 175, 125, 100, 75, 100, 50, 125, 150, 200],
    "site_visits": [5, 4, 5, 9, 6, 5, 4, 5, 3, 6, 7, 10]
}

# Create DataFrames
sales_df = pd.DataFrame(sales_data)
ad_df = pd.DataFrame(ad_data)

# Exploratory Data Analysis
# 1. Dataset Size
print("Size of the dataset:", sales_df.shape)

# 2. Types of Data
print("Data types in the dataset:\n", sales_df.dtypes)

# 3. Minimum and Maximum Order Totals
min_order_total = sales_df['order_total'].min()
max_order_total = sales_df['order_total'].max()
print(f"Minimum Order Total: {min_order_total}")
print(f"Maximum Order Total: {max_order_total}")

# 4. Visualization
plt.figure(figsize=(10, 6))
sns.histplot(sales_df['order_total'], bins=10, kde=True)
plt.title('Distribution of Order Totals')
plt.xlabel('Order Total ($)')
plt.ylabel('Frequency')
plt.show()

# 5. Feature Engineering
# Adding a column for day of the week
sales_df['sale_date'] = pd.to_datetime(sales_df['sale_date'] + '/2024', format='%m/%d/%Y')
sales_df['day_of_week'] = sales_df['sale_date'].dt.day_name()
print("Feature Engineering - Added Day of Week:\n", sales_df[['sale_date', 'day_of_week']])

# Chart Title
# Based on the chart of order totals vs. number of orders
chart_title = "Relationship Between Order Totals and Number of Orders"
print("Suggested Chart Title:", chart_title)

# 6. Chart Analysis
# Visualizing order totals vs. number of orders
plt.figure(figsize=(10, 6))
sns.scatterplot(data=sales_df, x='order_total', y='order_total', label='Order Count')
plt.title(chart_title)
plt.xlabel('Order Total ($)')
plt.ylabel('Number of Orders')
plt.show()

# 7. Range of Orders
# Assuming the 'order_total' column represents order values
order_range = sales_df['order_total'].describe()
print("Range of Orders:\n", order_range)

# 8. Correlations in Ad Spend Data
plt.figure(figsize=(10, 6))
sns.scatterplot(data=ad_df, x='social_ad_spend', y='site_visits')
plt.title('Site Visits vs. Social Media Ad Spend')
plt.xlabel('Social Media Ad Spend ($)')
plt.ylabel('Site Visits')
plt.show()

# Check for correlation
correlation = ad_df.corr().loc['social_ad_spend', 'site_visits']
print(f"Correlation between Social Media Ad Spend and Site Visits: {correlation}")

# Modeling: Linear Regression
X = ad_df[['social_ad_spend']]  # Features
y = ad_df['site_visits']         # Target variable

# Splitting data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Creating and training the Linear Regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Making predictions
y_pred = model.predict(X_test)

# Evaluating the model
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"Mean Squared Error: {mse}")
print(f"R-squared: {r2}")

# 9. Expected Site Visits Prediction
expected_ad_spend = 250
predicted_visits = model.predict([[expected_ad_spend]])
print(f"Expected Site Visits for ${expected_ad_spend} Ad Spend: {predicted_visits[0]}")

# 10. Model Sufficiency Evaluation
# The model's R-squared value can help assess its generalizability
if r2 > 0.7:
    model_sufficiency = "The model is sufficient for general use."
else:
    model_sufficiency = "The model may need improvement for general use."
print("Model Sufficiency Evaluation:", model_sufficiency)

# 11. Clustering Analysis Placeholder
# For clustering, additional analysis would be needed. 
# As an example, we might categorize customers based on spending habits.
# This would typically involve techniques like K-Means clustering.

# 12. Forecasting Model
forecasting_model = "For sales forecasting, a time series model such as ARIMA or Exponential Smoothing could be suitable."
print("Forecasting Model Recommendation:", forecasting_model)

# Answers to Questions
print("\n--- Questions and Answers ---")
print("1. What are some things you can tell about this dataset?")
print("   - The dataset has a size of:", sales_df.shape)
print("   - The dataset contains both numerical (e.g., order_total) and categorical data (e.g., item_category).")

print("2. What kind of data is in this dataset?")
print("   - The dataset includes numerical data (e.g., order_total, quant_items_per_order) and categorical data (e.g., item_category, customer_id).")

print("3. Minimum and Maximum values in order_total column:")
print(f"   - Minimum Order Total: {min_order_total}")
print(f"   - Maximum Order Total: {max_order_total}")

print("4. What kind of chart would you use to help visualize this data?")
print("   - A histogram or scatter plot would be suitable to visualize the distribution of order totals and their relationship with other variables.")

print("5. Would you add an additional column to this dataset using feature engineering?")
print("   - Yes, adding a 'day of the week' column would provide insights into sales patterns related to specific days.")

print("6. Based on the data in this chart, what would be a good title for this chart?")
print(f"   - Suggested Chart Title: {chart_title}")

print("7. What does this chart tell you about the number of orders in relation to the amount someone spends per order?")
print("   - The chart suggests that higher order totals may correspond to higher numbers of items purchased, indicating customer spending behavior.")

print("8. What range do most of the orders tend to be in?")
print("   - The order totals primarily range from the minimum to maximum values identified, with a frequency distribution that can be analyzed.")

print("9. Do you notice any correlations between the variables in this chart?")
print("   - Yes, there appears to be a positive correlation between social media ad spend and site visits, indicating that higher spending likely leads to more visits.")

print("10. Reviewing this linear regression model, roughly how many site visits can be expected if the marketing budget is increased to $250?")
print(f"   - Expected Site Visits for ${expected_ad_spend} Ad Spend: {predicted_visits[0]}")

print("11. Do you think the model is sufficient for general use for this data? Why or why not?")
print(f"   - {model_sufficiency}")

print("12. How would you describe the two different customer groups identified by the clustering algorithm?")
print("   - Further clustering analysis is needed to define the groups based on their spending habits, which could indicate different customer segments.")

print("13. What model might you use to forecast BrightThreads sales in the coming quarter? Why did you choose this?")
print(f"   - {forecasting_model}")
