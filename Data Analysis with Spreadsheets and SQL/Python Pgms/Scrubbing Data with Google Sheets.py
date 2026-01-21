import pandas as pd

# Load data
file_path = 'Activity Dataset_ Cleaning - Customer Data.csv'  # Replace with your CSV file path
df = pd.read_csv(file_path)

# Preview data
print("Initial data preview:")
print(df.head())

# 1. Remove duplicate rows
df = df.drop_duplicates()
print("\nDuplicates removed.")

# 2. Handle missing values
# Check for missing values in important columns
missing_counts = df[['Description', 'Price', 'Quantity']].isnull().sum()
print(f"\nMissing values before cleaning:\n{missing_counts}")

# Drop rows with missing critical info like Description or Price or Quantity
df = df.dropna(subset=['Description', 'Price', 'Quantity'])
print("\nRows with missing critical values removed.")

# 3. Convert columns to appropriate data types
df['Price'] = pd.to_numeric(df['Price'], errors='coerce')
df['Quantity'] = pd.to_numeric(df['Quantity'], errors='coerce')

# Drop rows where conversion to numeric failed (NaNs)
df = df.dropna(subset=['Price', 'Quantity'])

# 4. Remove invalid values
# Remove rows where Price or Quantity are negative (assuming negatives are invalid here)
df = df[(df['Price'] >= 0) & (df['Quantity'] >= 0)]
print("\nInvalid negative Price or Quantity rows removed.")

# 5. Final max value in Price column
max_price = df['Price'].max()
print(f"\nMaximum valid price after cleaning: {max_price}")

# Optionally save cleaned data
cleaned_file_path = 'Activity Dataset_ Cleaned - Customer Data.csv'
df.to_csv(cleaned_file_path, index=False)
print(f"\nCleaned data saved to {cleaned_file_path}")
