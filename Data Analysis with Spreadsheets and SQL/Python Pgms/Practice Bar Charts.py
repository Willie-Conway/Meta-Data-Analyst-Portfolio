import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
file_path = 'Activity Dataset_ Weeks 3-4 - Customer Data.csv'
df = pd.read_csv(file_path)

# Clean column names
df.columns = df.columns.str.strip()

# Drop rows with missing 'Description' or 'Quantity'
df = df.dropna(subset=['Description', 'Quantity'])

# Group by Description and sum Quantity to find most popular items
top_items = (
    df.groupby('Description')['Quantity']
    .sum()
    .sort_values(ascending=False)
    .head(10)  # Top 10 items
)

# Question 1
print("Answer to Question 1:\nYes")

# Question 2
second_top_item = top_items.index[1]
print("\nAnswer to Question 2:")
print(f"Second highest item sold: {second_top_item}")

# Create bar chart
plt.figure(figsize=(12, 6))
top_items.plot(kind='bar', color='skyblue')
plt.title('Top 10 Most Purchased Stock Items')
plt.ylabel('Total Quantity Sold')
plt.xlabel('Item Description')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()
