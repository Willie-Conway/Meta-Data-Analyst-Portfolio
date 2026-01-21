import pandas as pd
import random

# Generate 100 random home selling prices between 100,000 and 500,000
home_prices = [random.uniform(100000, 500000) for _ in range(100)]  # Use uniform for decimal values

# Generate random home sizes between 800 and 5000 square feet
home_sizes = [random.randint(800, 5000) for _ in range(100)]

# Create a DataFrame
df = pd.DataFrame({
    'Price': home_prices,
    'Size': home_sizes
})

# Format the 'Price' column with thousands separators and two decimal places
df['Price'] = df['Price'].apply(lambda x: f"{x:,.2f}")

# Save the DataFrame to a CSV file
df.to_csv('home_selling_prices.csv', index=False)

print("home_selling_prices.csv created with 100 entries.")

