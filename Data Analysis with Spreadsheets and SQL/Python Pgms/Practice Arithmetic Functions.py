import pandas as pd

# Load the dataset
file_path = 'Activity Dataset_ Weeks 3-4 - Customer Data.csv'
df = pd.read_csv(file_path)

# Ensure columns are correctly named if needed
df.columns = df.columns.str.strip()

# Create a new column for total cost: Quantity * Price
df['TotalCost'] = df['Quantity'] * df['Price']

# Filter the data for invoice 489447
invoice_total = df[df['Invoice'] == 489447]['TotalCost'].sum()

# Display the total cost for invoice 489447
print("Total cost for invoice 489447:", invoice_total)

# Question 1 Answer
print("\nAnswer to Question 1:")
print("Yes - Successfully used arithmetic operators (multiplication) to compute total cost.")

# Question 2 Answer
print("\nAnswer to Question 2:")
print(f"The total cost for invoice 489447 is: {int(invoice_total)}")
