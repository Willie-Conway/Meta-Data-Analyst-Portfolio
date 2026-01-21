import pandas as pd
import numpy as np
import hashlib

# Set the random seed for reproducibility
np.random.seed(42)

# Function to generate a hash code
def generate_hash(value):
    return hashlib.sha256(str(value).encode()).hexdigest()

# Generate random sample data
num_rows = 100  # Change to 100 rows
data = {
    'CustomerID': [generate_hash(i) for i in range(num_rows)],  # Generate hash for CustomerID
    'Age': np.random.randint(18, 80, size=num_rows).tolist()  # Age between 18 and 79
}

# Set a few customers' ages to 100
ages_to_replace = np.random.choice(range(num_rows), size=5, replace=False)  # Randomly choose 5 indices
for index in ages_to_replace:
    data['Age'][index] = 100

data.update({
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
    # Generate TotalCharges with some being exactly $100 and some slightly above
    'TotalCharges': [100.00] * 10 + [np.round(np.random.uniform(100.01, 120), 2) for _ in range(num_rows - 10)]
})

# Shuffle the TotalCharges to mix in the $100 values
np.random.shuffle(data['TotalCharges'])

# Create a DataFrame
customers_df = pd.DataFrame(data)

# Save the DataFrame to a CSV file named small_customers.csv
customers_df.to_csv('small_customers.csv', index=False)

print("small_customers.csv file created with 100 rows of sample data, including hash codes for CustomerID, Age field with some customers aged 100, and TotalCharges with some values at $100 and slightly above.")
