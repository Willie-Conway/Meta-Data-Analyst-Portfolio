import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
file_path = 'Activity Dataset_ Weeks 3-4 - Customer Data.csv'
df = pd.read_csv(file_path)

# Clean column names
df.columns = df.columns.str.strip()

# Drop rows with missing key data
df = df.dropna(subset=['InvoiceDate', 'Quantity'])

# Convert InvoiceDate to datetime
df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'], errors='coerce')
df = df.dropna(subset=['InvoiceDate'])

# Extract time of day as decimal hour (e.g., 14.5 for 2:30 PM)
df['Hour'] = df['InvoiceDate'].dt.hour + df['InvoiceDate'].dt.minute / 60

# Filter for valid quantities
df = df[df['Quantity'] > 0]

# Question 1
print("Answer to Question 1:\nYes")

# Scatter Plot: Hour vs Quantity
plt.figure(figsize=(10, 6))
plt.scatter(df['Hour'], df['Quantity'], alpha=0.5, edgecolors='k')
plt.title('Quantity of Items Ordered by Time of Day')
plt.xlabel('Hour of Day')
plt.ylabel('Quantity Ordered')
plt.grid(True)
plt.tight_layout()
plt.show()

# Question 2: Determine correlation
correlation = df[['Hour', 'Quantity']].corr().iloc[0, 1]
print("\nAnswer to Question 2:")
if correlation > 0.3:
    print("There is a positive correlation")
elif correlation < -0.3:
    print("There is a negative correlation")
else:
    print("There is no correlation")

print(f"\n(Correlation coefficient: {correlation:.2f})")
