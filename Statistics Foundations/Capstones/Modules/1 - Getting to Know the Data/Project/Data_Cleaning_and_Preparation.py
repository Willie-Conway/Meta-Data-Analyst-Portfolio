import pandas as pd
import numpy as np
import sqlite3

# Load the dataset
data = pd.read_csv('messy_dataset.csv')

# Display the initial structure of the data
print("Initial data structure:")
print(data.info())

# Check for and remove duplicate records
initial_count = data.shape[0]
data = data.drop_duplicates()
final_count = data.shape[0]
print(f"Removed {initial_count - final_count} duplicate rows.")

# Impute missing values
# Impute numeric columns with mean
numeric_columns = data.select_dtypes(include=['float64', 'int64']).columns
for column in numeric_columns:
    data[column].fillna(data[column].mean(), inplace=True)

# Impute categorical columns with mode
categorical_columns = data.select_dtypes(include=['object']).columns
for column in categorical_columns:
    data[column].fillna(data[column].mode()[0], inplace=True)

# Normalize data formats
# Convert text to lowercase
data[categorical_columns] = data[categorical_columns].apply(lambda x: x.str.lower())

# Standardize date formats (if applicable)
if 'Date' in data.columns:
    data['Date'] = pd.to_datetime(data['Date']).dt.strftime('%Y-%m-%d')

# Check for remaining missing values
print("\nMissing values after cleaning:")
print(data.isnull().sum())

# Save the cleaned data to a new CSV file
data.to_csv('cleaned_dataset.csv', index=False)
print("Cleaned dataset saved as 'cleaned_dataset.csv'.")

# Optionally, save cleaned data to SQL database
conn = sqlite3.connect('cleaned_data.db')
data.to_sql('cleaned_data', conn, if_exists='replace', index=False)
print("Cleaned data has been inserted into the SQL database 'cleaned_data.db'.")

# Function to add a new record
def add_record(new_record):
    global data
    data = data.append(new_record, ignore_index=True)
    print("New record added.")

# Function to update an existing record by Transaction_ID
def update_record(transaction_id, updated_values):
    global data
    index = data[data['Transaction_ID'] == transaction_id].index
    if index.empty:
        print("Transaction ID not found.")
    else:
        for key, value in updated_values.items():
            data.at[index[0], key] = value
        print("Record updated.")

# Example usage of add_record
new_record = {
    'Transaction_ID': 101,
    'Product_Name': 'Oranges',
    'Category': 'Fruit',
    'Quantity': 4,
    'Price': 0.4,
    'Total_Sales': 1.6,
    'Date': '2023-10-04'
}
add_record(new_record)

# Example usage of update_record
update_record(5, {'Quantity': 12, 'Total_Sales': 1.2})  # Updating the record with Transaction_ID 5

# Save the updated data to CSV
data.to_csv('updated_cleaned_dataset.csv', index=False)
print("Updated dataset saved as 'updated_cleaned_dataset.csv'.")

# Close the database connection
conn.close()
