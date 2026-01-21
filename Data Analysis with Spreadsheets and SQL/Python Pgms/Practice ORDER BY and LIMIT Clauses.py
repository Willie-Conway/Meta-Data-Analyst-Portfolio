import pandas as pd

# Load the dataset (adjust the path as needed)
file_path = 'Activity Dataset_ Weeks 3-4 - Customer Data.csv'
df = pd.read_csv(file_path)

# Sort by Price in descending order and select the top 10 items
top_10 = df[['StockCode', 'Description', 'Price']].sort_values(by='Price', ascending=False).drop_duplicates()
top_10 = top_10.head(10).reset_index(drop=True)

# Display the result
print("Top 10 highest-priced items:\n")
print(top_10)

# Identify the 3rd highest-priced item
third_item = top_10.iloc[2]['Description']

# Answer Question 1
print("\nAnswer to Question 1:")
print("Yes - Successfully replicated ORDER BY and LIMIT in Python using sort_values and head.")

# Answer Question 2
print("\nAnswer to Question 2:")
print(f"The third highest-priced item is: {third_item}")
