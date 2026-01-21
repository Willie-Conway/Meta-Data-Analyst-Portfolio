import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Generate dates
start_date = datetime(2018, 1, 1)
end_date = datetime(2022, 12, 31)
date_range = pd.date_range(start=start_date, end=end_date, freq='D')

# Randomly sample 200 unique dates
sampled_dates = np.random.choice(date_range, 200, replace=False)

# Generate random sales data and format it correctly
sales_data = np.random.randint(1000, 10000, size=200) + np.random.rand(200)  # Sales range from 1000 to 10000.99
sales_data = [f"{sales:,.2f}" for sales in sales_data]  # Format sales

# Create DataFrame
data = pd.DataFrame({
    'Date': sampled_dates,
    'Sales': sales_data
})

# Sort by date
data.sort_values('Date', inplace=True)

# Save to CSV without extra index column
data.to_csv('Time_Series_Data.csv', index=False)

print("Time_Series_Data.csv created successfully.")
