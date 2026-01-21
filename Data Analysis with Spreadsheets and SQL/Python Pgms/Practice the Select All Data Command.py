import pandas as pd

# Load the CSV file (update the path if needed)
file_path = 'Activity Dataset_ Weeks 3-4 - Customer Data.csv'
df = pd.read_csv(file_path)

# Preview the first 5 rows of the dataset (SELECT * equivalent)
print("=== All data preview ===")
print(df.head())

# Select a single column (like SELECT Description FROM table)
print("\n=== Descriptions only ===")
print(df['Description'].head())

# Select multiple columns (like SELECT Invoice, Description, Price FROM table)
print("\n=== Selected columns: Invoice, Description, Price ===")
print(df[['Invoice', 'Description', 'Price']].head())

# Example: filter rows where Customer ID is 13085
customer_id = 13085
print(f"\n=== Rows with Customer ID = {customer_id} ===")
print(df[df['Customer ID'] == customer_id].head())


