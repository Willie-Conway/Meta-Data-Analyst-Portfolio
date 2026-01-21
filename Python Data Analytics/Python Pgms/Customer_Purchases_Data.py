import pandas as pd
import numpy as np
import hashlib

# Set the random seed for reproducibility
np.random.seed(42)

# Function to generate a hash code
def generate_hash(value):
    return hashlib.sha256(str(value).encode()).hexdigest()

# Generate random sample data
num_rows = 100  # Set to 100 rows
customer_data = {
    'CustomerID': [generate_hash(i) for i in range(num_rows)],  # Generate hash for CustomerID
    'PaymentMethod': np.random.choice(
        ['Credit card (automatic)', 'Bank transfer (automatic)', 'Mailed check', 'Electronic check'],
        size=num_rows
    )
}

# Create a DataFrame for customers
customers_df = pd.DataFrame(customer_data)

# Create a new purchases DataFrame
purchases_data = {
    'CustomerID': customers_df['CustomerID'],  # Use CustomerID from the existing DataFrame
    'Age': np.random.randint(18, 70, size=num_rows),  # Random ages between 18 and 70
    'PaymentMethod': customers_df['PaymentMethod'],  # Use PaymentMethod from the existing DataFrame
    'Purchase': ['$' + np.round(np.random.uniform(5, 500), 2).astype(str) for _ in range(num_rows)]  # Add dollar sign to purchase amounts
}

# Create the purchases DataFrame
purchases_df = pd.DataFrame(purchases_data)

# Save the purchases DataFrame to a CSV file
purchases_df.to_csv('purchases.csv', index=False)

print("purchases.csv file created with 100 rows and the fields CustomerID, Age, PaymentMethod, and Purchase, including dollar signs in the Purchase amounts.")
