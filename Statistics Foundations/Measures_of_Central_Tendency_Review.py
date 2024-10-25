# Measures Of Central Tendency Review

import numpy as np
from collections import Counter

# Sample dataset: ages of customers
ages = [25, 30, 25, 32, 28, 25, 35, 40, 32, 30]

# Calculate the mean
def calculate_mean(data):
    """Calculate the mean of a dataset."""
    return np.mean(data)

# Calculate the median
def calculate_median(data):
    """Calculate the median of a dataset."""
    return np.median(data)

# Calculate the mode
def calculate_mode(data):
    """Calculate the mode of a dataset."""
    data_counter = Counter(data)
    mode_data = data_counter.most_common(1)  # Get the most common element
    return mode_data[0][0] if mode_data else None  # Return the mode

# Main function to display results
def main():
    mean_age = calculate_mean(ages)
    median_age = calculate_median(ages)
    mode_age = calculate_mode(ages)
    
    print(f"Mean Age: {mean_age}")
    print(f"Median Age: {median_age}")
    print(f"Mode Age: {mode_age}")

# Run the main function
if __name__ == "__main__":
    main()
