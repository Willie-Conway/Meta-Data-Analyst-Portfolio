import pandas as pd

# Load the dataset
file_path = 'Activity Dataset_ Weeks 3-4 - Customer Data.csv'
df = pd.read_csv(file_path)

# Clean column names just in case
df.columns = df.columns.str.strip()

# Drop any rows with missing values in Quantity or Price
df = df.dropna(subset=['Quantity', 'Price'])

# Question 1: Successfully used aggregate functions
print("Answer to Question 1:\nYes")

# Question 2: Calculate average quantity
average_quantity = round(df['Quantity'].mean(), 2)
print("\nAnswer to Question 2:")
print(f"The average quantity of items ordered is: {average_quantity}")

# Extra: Also calculating maximum price (not asked, but part of the activity)
max_price = df['Price'].max()
print(f"\nAdditional info: The maximum price of a given item is: {max_price}")
