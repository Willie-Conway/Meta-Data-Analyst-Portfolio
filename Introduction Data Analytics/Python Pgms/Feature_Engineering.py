# Feature Engineering

# Import necessary libraries
import pandas as pd
import numpy as np

# Step 1: Load Sample Data
# Creating a sample DataFrame to simulate customer data
data = {
    'customer_id': [1, 2, 3, 4, 5, 6],  # Unique identifier for each customer
    'age': [25, 30, 35, np.nan, 45, 50],  # Age of the customer; includes a missing value
    'gender': ['F', 'M', 'M', 'F', 'M', np.nan],  # Gender of the customer; includes a missing value
    'purchase_amount': [200, 150, np.nan, 300, 400, 250],  # Purchase amounts; includes a missing value
    'signup_date': pd.to_datetime(['2020-01-01', '2020-05-01', '2021-01-01', '2021-05-01', '2022-01-01', '2022-05-01'])  # Dates customers signed up
}

# Create a DataFrame
df = pd.DataFrame(data)

# Step 2: Display the original data
print("Original Data:")
print(df)

# Step 3: Handle Missing Values
# Fill missing values for 'age' with the median age
df['age'].fillna(df['age'].median(), inplace=True)  # Ensures age has no missing values

# Fill missing values for 'purchase_amount' with the mean purchase amount
df['purchase_amount'].fillna(df['purchase_amount'].mean(), inplace=True)  # Ensures purchase amount has no missing values

# Fill missing values for 'gender' with the mode
df['gender'].fillna(df['gender'].mode()[0], inplace=True)  # Ensures gender has no missing values

# # Feature Engineering
# Step 4: Encode Categorical Variables
# Convert 'gender' into numeric format using one-hot encoding
df = pd.get_dummies(df, columns=['gender'], drop_first=True)  # Creates binary columns for gender

# Step 5: Create New Features
# Calculate the number of days since signup
df['days_since_signup'] = (pd.to_datetime('today') - df['signup_date']).dt.days  # New feature for time since signup

# Step 6: Drop unnecessary columns
# Remove customer_id and signup_date as they are not needed for analysis
df.drop(columns=['customer_id', 'signup_date'], inplace=True)  # Clean up the DataFrame

# Step 7: Display the cleaned and transformed data
print("\nTransformed Data:")
print(df)

# Step 8: Save the transformed data to a new CSV file (optional)
df.to_csv('transformed_data.csv', index=False)  # Export cleaned data to a CSV file
