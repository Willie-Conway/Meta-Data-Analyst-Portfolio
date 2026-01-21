import pandas as pd

# Load the dataset
file_path = 'Activity Dataset_ Weeks 3-4 - Customer Data.csv'
df = pd.read_csv(file_path)

# Clean column names
df.columns = df.columns.str.strip()

# Drop any rows with missing Country or Invoice
df = df.dropna(subset=['Country', 'Invoice'])

# Group by Country and count unique invoices (orders)
orders_by_country = df.groupby('Country')['Invoice'].nunique().reset_index(name='Order Count')

# Question 1
print("Answer to Question 1:\nYes")

# Question 2
germany_orders = orders_by_country[orders_by_country['Country'] == 'Germany']['Order Count'].values[0]
print("\nAnswer to Question 2:")
print(f"Number of orders from Germany: {germany_orders}")

# Optional: Display all countries and order counts
print("\nOrders by Country:")
print(orders_by_country.sort_values(by='Order Count', ascending=False))
