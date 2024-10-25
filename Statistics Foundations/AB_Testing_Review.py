# AB_Testing_Review.py

import pandas as pd
import numpy as np
from scipy import stats

# Task 1: Create a CSV file with simulated data
data = {
    'color_scheme': np.random.choice(['red', 'blue'], size=1000),
    'conversion': np.random.choice([0, 1], size=1000, p=[0.7, 0.3])  # 30% conversion rate for example
}

# Introduce bias towards blue for demonstration
data['conversion'][data['color_scheme'] == 'blue'] = np.random.choice([0, 1], size=(data['color_scheme'] == 'blue').sum(), p=[0.6, 0.4])  # 40% conversion rate for blue

df = pd.DataFrame(data)
df.to_csv('website_color_test.csv', index=False)

# Task 2: Load the data
df = pd.read_csv('website_color_test.csv')

# Task 3: Formulate Hypotheses
# H0: There is no difference in conversion rates between red and blue.
# H1: There is a difference in conversion rates between red and blue.

# Task 4: Perform the A/B Test
# Group by color scheme and calculate conversion rates
conversion_rates = df.groupby('color_scheme')['conversion'].mean()
print("Conversion Rates:\n", conversion_rates)

# Perform Chi-squared test
contingency_table = pd.crosstab(df['color_scheme'], df['conversion'])
chi2, p, dof, expected = stats.chi2_contingency(contingency_table)

# Task 5: Interpret Results
alpha = 0.05  # significance level
if p < alpha:
    print(f"Reject the null hypothesis (p-value = {p:.4f}). There is a significant difference in conversion rates.")
else:
    print(f"Fail to reject the null hypothesis (p-value = {p:.4f}). There is no significant difference in conversion rates.")
