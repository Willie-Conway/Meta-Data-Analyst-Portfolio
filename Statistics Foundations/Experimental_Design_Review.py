# Experimental Design Review
# Import necessary libraries
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import scipy.stats as stats

# Set random seed for reproducibility
np.random.seed(42)

# Step 1: Questioning
# Evaluation question: Does changing the website color scheme (A vs B) affect the number of sales?

# Step 2: Hypothesis
# Hypothesis: Sales will increase (change) with the color scheme B (how) compared to color scheme A (cause).

# Step 3: Required Variables
# Independent Variable: Color Scheme (A or B)
# Dependent Variable: Number of Sales

# Simulate data for A/B test
n_samples = 1000  # Sample size for each group
sales_A = np.random.poisson(lam=20, size=n_samples)  # Sales for Color Scheme A
sales_B = np.random.poisson(lam=25, size=n_samples)  # Sales for Color Scheme B

# Create a DataFrame for easier manipulation
data = pd.DataFrame({
    'Color_Scheme': ['A'] * n_samples + ['B'] * n_samples,
    'Sales': np.concatenate([sales_A, sales_B])
})

# Step 4: Choosing a Measurement Approach
# Here we are using an A/B test approach with Poisson-distributed sales data

# Step 5: Selecting an Analysis
# We'll perform a t-test to see if there's a significant difference in sales between the two groups
t_stat, p_value = stats.ttest_ind(sales_A, sales_B)

# Print the t-test results
print(f'T-statistic: {t_stat:.2f}, P-value: {p_value:.4f}')

# Plotting the results
plt.figure(figsize=(12, 6))

# Boxplot for Sales by Color Scheme
plt.subplot(1, 2, 1)
sns.boxplot(x='Color_Scheme', y='Sales', data=data)
plt.title('Sales by Color Scheme')
plt.ylabel('Number of Sales')
plt.xlabel('Color Scheme')

# Histogram for Sales distribution
plt.subplot(1, 2, 2)
sns.histplot(data=data, x='Sales', hue='Color_Scheme', bins=30, kde=True, stat='density', common_norm=False)
plt.title('Sales Distribution by Color Scheme')
plt.xlabel('Number of Sales')
plt.ylabel('Density')

# Show the plots
plt.tight_layout()
plt.show()
