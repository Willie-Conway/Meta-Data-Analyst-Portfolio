import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
file_path = 'Activity Dataset_ Weeks 3-4 - Customer Data.csv'
df = pd.read_csv(file_path)

# Clean up column names
df.columns = df.columns.str.strip()

# Drop rows with missing data in essential columns
df = df.dropna(subset=['Description', 'Quantity'])

# Group by item description and sum the quantities
item_counts = (
    df.groupby('Description')['Quantity']
    .sum()
    .sort_values(ascending=False)
    .head(5)  # Top 5 items for a readable pie chart
)

# Question 1
print("Answer to Question 1:\nYes")

# Question 2
top_item = item_counts.idxmax()
print("\nAnswer to Question 2:")
print(f"Highest item sold: {top_item}")

# Create pie chart
plt.figure(figsize=(8, 8))
item_counts.plot.pie(
    autopct='%1.1f%%',
    startangle=140,
    shadow=True,
    colors=plt.cm.Pastel1.colors,
)
plt.title('Top 5 Most Purchased Stock Items')
plt.ylabel('')  # Hide y-label for pie chart
plt.tight_layout()
plt.show()
