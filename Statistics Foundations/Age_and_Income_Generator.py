# Age_and_Income_Generator.py

import pandas as pd
import numpy as np

# Set random seed for reproducibility
np.random.seed(42)

# Generate random ages between 18 and 70
ages = np.random.randint(18, 71, size=100)

# Generate random incomes between 20.0000 and 120.0000
incomes = np.random.uniform(20.0000, 120.0000, size=100).round(4)

# Create a DataFrame
data = pd.DataFrame({
    'Age': ages,
    'Income': incomes
})

# Save to CSV
data.to_csv('Age_Income_Dataset.csv', index=False)

# Display the first few rows
print(data.head())
