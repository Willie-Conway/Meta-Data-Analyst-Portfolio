# Simple Linear Regression Review 

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression

# Generate sample data
np.random.seed(42)
# Independent variable: Adware Ad Clicks
ad_clicks = np.random.randint(1, 100, size=100)  # 100 random clicks between 1 and 100
# Dependent variable: Adware Ad Conversions (with some noise)
ad_conversions = 0.1 * ad_clicks + np.random.normal(0, 5, size=100)  # Linear relationship with noise

# Create a DataFrame
data = pd.DataFrame({
    'Ad Clicks': ad_clicks,
    'Ad Conversions': ad_conversions
})

# Check for the assumptions of SLR

# 1. Minimum sample size of 20
assert len(data) >= 20, "Sample size must be at least 20."

# 2. Linearity
sns.scatterplot(x='Ad Clicks', y='Ad Conversions', data=data)
plt.title('Scatter Plot of Ad Clicks vs. Ad Conversions')
plt.xlabel('Ad Clicks')
plt.ylabel('Ad Conversions')
plt.show()

# 3. Fit a linear regression model
X = data[['Ad Clicks']]  # Independent variable
y = data['Ad Conversions']  # Dependent variable

# Create and fit the model
model = LinearRegression()
model.fit(X, y)

# 4. Predict values
data['Predicted Conversions'] = model.predict(X)

# 5. Visualization with the trend line
plt.figure(figsize=(10, 6))
sns.scatterplot(x='Ad Clicks', y='Ad Conversions', data=data, label='Actual Data')
plt.plot(data['Ad Clicks'], data['Predicted Conversions'], color='red', label='Trend Line', linewidth=2)
plt.title('Simple Linear Regression: Ad Clicks vs. Ad Conversions')
plt.xlabel('Ad Clicks')
plt.ylabel('Ad Conversions')
plt.legend()
plt.show()

# 6. Making predictions
# Example: Predict conversions for 60 ad clicks
new_clicks = np.array([[60]])  # New data point for prediction
predicted_conversion = model.predict(new_clicks)
print(f'Predicted Ad Conversions for 60 Ad Clicks: {predicted_conversion[0]:.4f}')
