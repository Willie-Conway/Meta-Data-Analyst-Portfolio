# Reshaping Data with Transformations
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Set random seed for reproducibility
np.random.seed(42)

# Function to generate a skewed dataset
def generate_skewed_data(size, skew_type='positive'):
    if skew_type == 'positive':
        return np.random.exponential(scale=1, size=size)  # Positive skew
    elif skew_type == 'negative':
        return -np.random.exponential(scale=1, size=size)  # Negative skew
    else:
        return np.random.normal(loc=0, scale=1, size=size)  # Normal distribution

# Generate datasets
size = 100
data_positive_skew = generate_skewed_data(size, 'positive')

# Generate kurtosis dataset using Laplace distribution
data_high_kurtosis = np.random.laplace(loc=0, scale=1, size=size)

# Logarithmic Transformation
log_transformed = np.log10(data_positive_skew + 1)  # Add 1 to avoid log(0)

# Cube Root Transformation
cube_root_transformed = np.cbrt(data_positive_skew)

# Square Root Transformation
square_root_transformed = np.sqrt(data_positive_skew)

# Create DataFrames for each transformation
df_logs = pd.DataFrame({
    "Data Before Log Transformation": data_positive_skew,
    "Data after Log Transformation": log_transformed
})

df_cube_root = pd.DataFrame({
    "Data Before Cube Root Transformation": data_positive_skew,
    "Data after Cube Root Transformation": cube_root_transformed
})

df_square_root = pd.DataFrame({
    "Data Before Square Root Transformation": data_positive_skew,
    "Data after Square Root Transformation": square_root_transformed
})

# Save DataFrames to CSV
df_logs.to_csv("Data_Logs.csv", index=False)
df_cube_root.to_csv("Data_Cube_Root.csv", index=False)
df_square_root.to_csv("Data_Square_Root.csv", index=False)

# Create DataFrame for high kurtosis data
df_kurtosis = pd.DataFrame({
    "Data Before Kurtosis Transformation": data_high_kurtosis
})

# Save kurtosis dataset to CSV
df_kurtosis.to_csv("Data_High_Kurtosis.csv", index=False)

# Generate frequency tables
freq_table_logs = df_logs.value_counts().reset_index(name='Frequency')
freq_table_cube_root = df_cube_root.value_counts().reset_index(name='Frequency')
freq_table_square_root = df_square_root.value_counts().reset_index(name='Frequency')

# Print frequency tables
print("Frequency Table for Log Transformation:")
print(freq_table_logs)

print("\nFrequency Table for Cube Root Transformation:")
print(freq_table_cube_root)

print("\nFrequency Table for Square Root Transformation:")
print(freq_table_square_root)

# Function to plot histograms
def plot_histogram(data, title, xlabel):
    plt.figure(figsize=(10, 6))
    sns.histplot(data, bins=20, kde=True)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel('Frequency')
    plt.show()

# Plot histograms for original and transformed data
plot_histogram(data_positive_skew, 'Original Data (Positive Skew)', 'Value')
plot_histogram(log_transformed, 'Log Transformed Data', 'Log Value')
plot_histogram(cube_root_transformed, 'Cube Root Transformed Data', 'Cube Root Value')
plot_histogram(square_root_transformed, 'Square Root Transformed Data', 'Square Root Value')

# Plot histogram for high kurtosis dataset
plot_histogram(data_high_kurtosis, 'High Kurtosis Data (Laplace Distribution)', 'Value')
