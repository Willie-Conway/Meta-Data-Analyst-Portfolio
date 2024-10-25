import pandas as pd
import numpy as np

# Define the number of rows
num_rows = 5000

# Generate random data
data = {
    'longitude': np.random.uniform(-123.0, -121.0, num_rows).astype(float),
    'latitude': np.random.uniform(37.0, 38.5, num_rows).astype(float),
    'housing_median_age': np.round(np.random.uniform(17.0, 51.5, num_rows), 1).astype(float),  # Float with one decimal
    'total_rooms': np.round(np.random.uniform(100, 4842, num_rows)).astype(float),  # Float
    'total_bedrooms': np.round(np.random.uniform(100, 1001, num_rows)).astype(float),  # Float
    'population': np.round(np.random.uniform(200, 3001, num_rows)).astype(float),  # Float
    'households': np.round(np.random.uniform(100, 996, num_rows)).astype(float),  # Float
    'median_income': np.round(np.random.uniform(100000.01, 900000.06, num_rows), 2).astype(float),
    'ocean_proximity': np.random.choice(['NEAR BAY', '<1H OCEAN', 'INLAND', 'NEAR OCEAN', 'ISLAND'], num_rows),
    'median_house_value': np.round(np.random.uniform(300000, 1200001, num_rows)).astype(float)  # Float
}

# Create DataFrame
df = pd.DataFrame(data)

# Save to CSV
df.to_csv('bay_area_homes.csv', index=False)
