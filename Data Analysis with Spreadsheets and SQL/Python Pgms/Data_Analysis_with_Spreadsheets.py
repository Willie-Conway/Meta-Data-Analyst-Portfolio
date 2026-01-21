# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load data (replace this with your actual data source)
# Sample data creation for demonstration
data = {
    'Date': pd.date_range(start='2023-01-01', periods=10, freq='D'),
    'Sales': [150, 200, np.nan, 250, 300, 400, 350, 500, 450, 600],
    'Category': ['A', 'B', 'A', 'B', 'A', 'B', 'A', 'B', 'A', 'B']
}

df = pd.DataFrame(data)

# Step 1: Scrubbing Data

# 1. Accessing and Labeling Data
# Ensure columns are labeled and descriptive
df.columns = ['Date', 'Sales', 'Category']

# 2. Cleaning Data
# Remove duplicates (if any)
df = df.drop_duplicates()

# Handle missing data
df['Sales'].fillna(df['Sales'].mean(), inplace=True)  # Replace NaN with mean

# 3. Formatting Data
# Format date as string for consistency
df['Date'] = df['Date'].dt.strftime('%Y-%m-%d')

# Step 2: Exploring Data

# 1. Filtering and Sorting Data
# Filter sales greater than 300
filtered_data = df[df['Sales'] > 300]

# Sort data by Sales
sorted_data = df.sort_values(by='Sales')

# 2. Exploring Data with Functions
total_sales = df['Sales'].sum()
average_sales = df['Sales'].mean()
median_sales = df['Sales'].median()
max_sales = df['Sales'].max()
min_sales = df['Sales'].min()

# Print summary statistics
print("Total Sales:", total_sales)
print("Average Sales:", average_sales)
print("Median Sales:", median_sales)
print("Max Sales:", max_sales)
print("Min Sales:", min_sales)

# Step 3: Exploring Data Visually

# Create a bar chart for Sales by Category
plt.figure(figsize=(10, 5))
df.groupby('Category')['Sales'].sum().plot(kind='bar', color='skyblue')
plt.title('Total Sales by Category')
plt.xlabel('Category')
plt.ylabel('Total Sales')
plt.xticks(rotation=0)
plt.grid(axis='y')
plt.show()

# Create a line graph for Sales over Time
plt.figure(figsize=(10, 5))
plt.plot(df['Date'], df['Sales'], marker='o', color='orange')
plt.title('Sales Over Time')
plt.xlabel('Date')
plt.ylabel('Sales')
plt.xticks(rotation=45)
plt.grid()
plt.show()

# Step 4: Modeling Data

# Example: Simple linear regression model
from sklearn.linear_model import LinearRegression

# Prepare data for modeling
X = np.array(range(len(df))).reshape(-1, 1)  # Use index as independent variable
y = df['Sales'].values  # Sales as dependent variable

# Create and fit the model
model = LinearRegression()
model.fit(X, y)

# Predict sales using the model
predictions = model.predict(X)

# Plot the predictions
plt.figure(figsize=(10, 5))
plt.scatter(X, y, color='blue', label='Actual Sales')
plt.plot(X, predictions, color='red', label='Predicted Sales', linewidth=2)
plt.title('Sales Predictions using Linear Regression')
plt.xlabel('Index')
plt.ylabel('Sales')
plt.legend()
plt.grid()
plt.show()

# Conclusion
print("Spreadsheets are powerful tools for data analysis, but Python offers greater flexibility for data handling and analysis.")
