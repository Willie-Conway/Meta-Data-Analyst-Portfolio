import pandas as pd

# Load the dataset (adjust the path if needed)
file_path = 'Activity Dataset_ Weeks 3-4 - Customer Data.csv'
df = pd.read_csv(file_path)

# Filter data for Price between $1 and $5 inclusive
filtered_df = df[(df['Price'] >= 1) & (df['Price'] <= 5)]

# Select only Description and Quantity columns
result_df = filtered_df[['Description', 'Quantity']]

# Display the first 10 rows for review
print("Sample rows with Price between $1 and $5:\n")
print(result_df.head(10))

# Count how many rows match the filter
row_count = len(result_df)

print(f"\nTotal rows where price is between $1 and $5: {row_count}")

# Answer to Question 1
# Were you able to successfully use the AND, OR, and WHERE clauses in Google Sheets?
print("\nAnswer to Question 1:")
print("Yes - The Python script successfully applies AND (&) for filtering Price between $1 and $5.")

# Answer to Question 2
print("\nAnswer to Question 2:")
print(f"The number of rows returned by the query is: {row_count}")
# Based on your data, you can replace this number with the actual count if you have it (e.g., 1314, 158, 563, or 10)
