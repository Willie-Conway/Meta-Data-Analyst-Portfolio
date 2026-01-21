import pandas as pd
import numpy as np

# Define the number of rows
n_rows = 333

# Generate random data
data = {
    'customer_group': np.random.choice(['Group A', 'Group B', 'Group C'], n_rows),
    'location': np.random.choice(['Urban', 'Suburban', 'Rural'], n_rows),
    'n_days_member': np.random.randint(1, 365, n_rows),  # Days as a member
    'n_avg_items_browsed_per_week': np.random.randint(1, 50, n_rows),  # Items browsed
    'amount_spent': np.round(np.random.uniform(10.0, 500.0, n_rows), 2),  # Amount spent
    'device': np.random.choice(['Mobile', 'Desktop', 'Tablet'], n_rows)
}

# Create a DataFrame
df = pd.DataFrame(data)

# Save to CSV
df.to_csv('butler_customers.csv', index=False)

print("CSV file 'butler_customers.csv' created with 333 rows.")
