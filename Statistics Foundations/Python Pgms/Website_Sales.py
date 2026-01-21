# Website sales.py

import pandas as pd
import numpy as np

# Generate sample data
np.random.seed(0)  # For reproducibility
weeks = list(range(1, 101))  # Weeks 1 to 100
website_sales = np.random.uniform(100.00, 400.00, size=100).round(2)  # Random sales data

# Create DataFrame
data = {
    "Week": weeks,
    "Website Sales": website_sales
}
df = pd.DataFrame(data)

# Calculate statistics
sample_size = df['Website Sales'].count()  # Sample size
mean_sales = df['Website Sales'].mean()  # Mean sales
std_dev = df['Website Sales'].std()  # Standard deviation

# Confidence interval calculation
alpha = 0.05  # Alpha value for 95% confidence interval
z_score = 1.96  # Z-score for 95% confidence interval (approx.)
margin_of_error = z_score * (std_dev / np.sqrt(sample_size))

# Confidence interval values
lower_ci = mean_sales - margin_of_error
upper_ci = mean_sales + margin_of_error

# Add statistical results to the DataFrame
df_stats = pd.DataFrame({
    "Sample Size": [sample_size],
    "Standard Deviation": [std_dev],
    "95% Confidence Interval": [margin_of_error],
    "Lower C.I. Value": [lower_ci],
    "Upper C.I. Value": [upper_ci]
})

# Save to CSV
df.to_csv('website_sales.csv', index=False)
df_stats.to_csv('website_sales_stats.csv', index=False)

print("CSV files created: 'website_sales.csv' and 'website_sales_stats.csv'")
