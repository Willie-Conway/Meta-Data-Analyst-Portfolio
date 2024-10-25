import pandas as pd
import numpy as np
import hashlib

# Set the random seed for reproducibility
np.random.seed(42)

# Function to generate a hash code
def generate_hash(value):
    return hashlib.sha256(str(value).encode()).hexdigest()

# Generate random sample data
num_rows = 3827
data = {
    'CustomerID': [generate_hash(i) for i in range(num_rows)],  # Generate hash for CustomerID
    'gender': np.random.choice(['Female', 'Male'], size=num_rows),
    'SeniorCitizen': np.random.choice([0, 1], size=num_rows),
    'Partner': np.random.choice(['Yes', 'No'], size=num_rows),
    'Dependents': np.random.choice(['Yes', 'No'], size=num_rows),
    'Tenure': np.random.randint(0, 73, size=num_rows),  # Tenure between 0 and 72 months
    'PhoneService': np.random.choice(['Yes', 'No'], size=num_rows),
    'MultipleLines': np.random.choice(['Yes', 'No'], size=num_rows),
    'InternetService': np.random.choice(['DSL', 'Fiber optic', 'No'], size=num_rows),
    'DeviceProtection': np.random.choice(['Yes', 'No'], size=num_rows),  # New field
    'PaperlessBilling': np.random.choice(['Yes', 'No'], size=num_rows),
    'PaymentMethod': np.random.choice(
        ['Credit card (automatic)', 'Bank transfer (automatic)', 'Mailed check', 'Electronic check'],
        size=num_rows
    ),
    'TotalCharges': ['$' + np.round(np.random.uniform(0, 2000), 2).astype(str) for _ in range(num_rows)]
}

# Create a DataFrame
customers_df = pd.DataFrame(data)

# Save the DataFrame to a CSV file
customers_df.to_csv('customers.csv', index=False)

print("customers.csv file created with 3827 rows of sample data, including hash codes for CustomerID and DeviceProtection field.")
