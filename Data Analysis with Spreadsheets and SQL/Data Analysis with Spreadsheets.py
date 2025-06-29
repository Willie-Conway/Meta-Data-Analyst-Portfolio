import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
file_path = 'transactions-pet_store-small.csv'  # Update to your actual CSV path
df = pd.read_csv(file_path)

print("Initial data shape:", df.shape)

# -----------------
# SCRUB PHASE
# -----------------

# 1. Identify errors:

# Check for duplicates
duplicates = df[df.duplicated()]
print(f"Number of duplicate rows: {len(duplicates)}")
print("Sample duplicate rows:\n", duplicates.head())

# Check for missing values
missing_values = df.isnull().sum()
print("Missing values per column:\n", missing_values)

# Check obviously wrong values
# For example, Price should be positive, Quantity positive integers
wrong_prices = df[df['Price'] <= 0]
wrong_quantities = df[df['Quantity'] <= 0]
print("Rows with non-positive prices:\n", wrong_prices)
print("Rows with non-positive quantities:\n", wrong_quantities)

# Answer (example):
print("\n--- SCRUB Answers ---")
print("1. Errors identified:")
print("- Duplicate transaction data on rows: ", duplicates.index.tolist())
print("- Missing Product_Name in multiple rows (e.g., rows 0 and 1)")
print("- Zero or negative Price or Quantity values (none found in sample data, but should be checked)")

# Fixes:
# Remove duplicates
df_clean = df.drop_duplicates()
print(f"Data shape after dropping duplicates: {df_clean.shape}")

# Fill missing Product_Name with 'Unknown' or drop rows
df_clean['Product_Name'].fillna('Unknown', inplace=True)

# Remove rows with zero or negative Quantity or Price if any (none here)
df_clean = df_clean[(df_clean['Price'] > 0) & (df_clean['Quantity'] > 0)]

print("Data shape after cleaning: ", df_clean.shape)
print("Missing values after cleaning:\n", df_clean.isnull().sum())

print("\n- Fixes applied:")
print("- Removed duplicate rows")
print("- Filled missing Product_Name with 'Unknown'")
print("- Filtered out rows with invalid Price or Quantity")

# -----------------
# EXPLORE PHASE
# -----------------

# Calculate average price of items
average_price = df_clean['Price'].mean()
print(f"\nAverage Price of items: ${average_price:.2f}")

# Calculate correlation between Price and Quantity
correlation = df_clean[['Price', 'Quantity']].corr().iloc[0,1]
print(f"Correlation between Price and Quantity: {correlation:.2f}")

# Example SQL-like queries with pandas

# Query 1: ORDER BY Price DESC LIMIT 5 (Top 5 most expensive products)
top5_expensive = df_clean.sort_values(by='Price', ascending=False).head(5)
print("\nTop 5 most expensive products:\n", top5_expensive[['Product_Name', 'Price']])

# Query 2: WHERE Product_Category = 'dog' AND Quantity > 1
dog_multiple_qty = df_clean[(df_clean['Product_Category'] == 'dog') & (df_clean['Quantity'] > 1)]
print("\nDog products with quantity > 1:\n", dog_multiple_qty[['Product_Name', 'Quantity']])

# Query 3: GROUP BY Product_Category SUM(Quantity)
category_sales = df_clean.groupby('Product_Category')['Quantity'].sum().sort_values(ascending=False)
print("\nTotal quantity sold by product category:\n", category_sales)

print("\n--- EXPLORE Answers ---")
print("- Spreadsheet functions used: AVERAGE (Price), CORREL (Price, Quantity), SUM (Quantity)")
print(f"  - Average Price = ${average_price:.2f}")
print(f"  - Correlation Price & Quantity = {correlation:.2f}")
print("- SQL-like queries used:")
print("  1) ORDER BY Price DESC LIMIT 5 to find most expensive products")
print("  2) WHERE Product_Category = 'dog' AND Quantity > 1 to filter specific sales")
print("  3) GROUP BY Product_Category to sum quantities sold")

# -----------------
# VISUALIZE PHASE
# -----------------

sns.set(style="whitegrid")

# Chart 1: Bar chart of total quantity sold by Product_Category
plt.figure(figsize=(10,6))
category_sales.plot(kind='bar', color='skyblue')
plt.title('Total Quantity Sold by Product Category')
plt.xlabel('Product Category')
plt.ylabel('Total Quantity Sold')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('bar_quantity_by_category.png')
plt.show()

# Chart 2: Scatter plot of Price vs Quantity
plt.figure(figsize=(10,6))
sns.scatterplot(data=df_clean, x='Price', y='Quantity', hue='Product_Category', palette='deep', alpha=0.7)
plt.title('Scatter Plot: Price vs Quantity')
plt.xlabel('Price')
plt.ylabel('Quantity')
plt.tight_layout()
plt.savefig('scatter_price_vs_quantity.png')
plt.show()

print("\nDashboard Creation Instructions:")
print("- Create a Tableau Public dashboard including at least two charts (e.g., the above bar chart and scatter plot).")
print("- Add interactivity such as filters by Product_Category or Date.")
print("- Publish your dashboard to Tableau Public.")
print("- Copy and paste your Tableau Public dashboard URL here.")

print("\nExample: https://public.tableau.com/views/YourDashboardName/Sheet1")

# -----------------
# END OF SCRIPT
# -----------------
