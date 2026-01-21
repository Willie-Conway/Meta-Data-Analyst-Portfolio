# False_Positives_and_False_Negatives.py

import numpy as np
import scipy.stats as stats

# Set the seed for reproducibility
np.random.seed(42)

# Generate synthetic data for two groups
# Group A (e.g., website color red)
group_a = np.random.normal(loc=50, scale=10, size=100)

# Group B (e.g., website color blue)
group_b = np.random.normal(loc=55, scale=10, size=100)

# Perform a t-test to compare the means of two groups
t_statistic, p_value = stats.ttest_ind(group_a, group_b)

# Define significance level
alpha = 0.05

# Print results
print(f"T-statistic: {t_statistic}")
print(f"P-value: {p_value}")

# Hypothesis Testing
# H0: There is no difference in sales between website colors (means are equal)
# H1: There is a difference in sales between website colors (means are not equal)

# Check if we reject the null hypothesis
if p_value < alpha:
    print("Reject the null hypothesis (H0). We conclude there is a difference (H1).")
    # Possible Type I Error (False Positive)
    print("Warning: This could be a false positive if H0 is actually true.")
else:
    print("Fail to reject the null hypothesis (H0). We conclude there is no difference.")
    # Possible Type II Error (False Negative)
    print("Warning: This could be a false negative if H1 is actually true.")

# To demonstrate Type I and Type II errors, let's define true conditions
true_effect = 5  # True difference in means
# Simulate data under the null hypothesis (no difference)
null_group_a = np.random.normal(loc=50, scale=10, size=100)
null_group_b = np.random.normal(loc=50, scale=10, size=100)

# Perform t-test under null hypothesis
null_t_statistic, null_p_value = stats.ttest_ind(null_group_a, null_group_b)

# Check for Type I Error (False Positive)
if null_p_value < alpha:
    print("Type I Error: We incorrectly rejected H0 when it was true.")

# Simulate data where H1 is true (there is a difference)
alt_group_a = np.random.normal(loc=50, scale=10, size=100)
alt_group_b = np.random.normal(loc=55, scale=10, size=100)

# Perform t-test under alternative hypothesis
alt_t_statistic, alt_p_value = stats.ttest_ind(alt_group_a, alt_group_b)

# Check for Type II Error (False Negative)
if alt_p_value >= alpha:
    print("Type II Error: We incorrectly failed to reject H0 when H1 is true.")

# Conclusion
print("Analysis complete. Remember that hypothesis testing involves probabilities, and errors can occur.")
