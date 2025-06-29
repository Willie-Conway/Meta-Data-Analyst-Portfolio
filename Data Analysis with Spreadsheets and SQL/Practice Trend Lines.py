import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
file_path = 'Activity Dataset_ Weeks 3-4 - Customer Data.csv'
df = pd.read_csv(file_path)

# Clean up column names
df.columns = df.columns.str.strip()

# Drop rows with missing data in key columns
df = df.dropna(subset=['InvoiceDate', 'Quantity', 'Price'])

# Convert InvoiceDate to datetime
df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'], errors='coerce')

# Remove rows with invalid or missing dates
df = df.dropna(subset=['InvoiceDate'])

# Create a total price column
df['Total'] = df['Quantity'] * df['Price']

# Group by date (daily total sales)
daily_sales = df.groupby(df['InvoiceDate'].dt.date)['Total'].sum()

# Question 1
print("Answer to Question 1:\nYes")

# Question 2
peak_date = daily_sales.idxmax()
print("\nAnswer to Question 2:")
print(f"Sales peaked on: {peak_date}")

# Plot the trend chart
plt.figure(figsize=(12, 6))
daily_sales.plot(kind='line', marker='o', linestyle='-')
plt.title('Daily Sales Trend Over Time')
plt.xlabel('Date')
plt.ylabel('Total Sales')
plt.grid(True)
plt.tight_layout()
plt.show()
