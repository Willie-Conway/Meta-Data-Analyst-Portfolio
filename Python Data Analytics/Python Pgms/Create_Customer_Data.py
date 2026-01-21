import pandas as pd
import numpy as np

# Create a sample customer data
customer_data = {
    'customer_id': range(1, 101),
    'email': [f'customer{i}@example.com' for i in range(1, 101)],
    'name': [f'Customer {i}' for i in range(1, 101)],
    'purchase_amount': np.random.randint(20, 100, size=100)
}

# Create DataFrame
df = pd.DataFrame(customer_data)

# Save to CSV
df.to_csv('customer_data.csv', index=False)

print("customer_data.csv created successfully.")
