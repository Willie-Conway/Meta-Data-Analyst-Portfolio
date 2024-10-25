# Chooding A Model Review.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm
from sklearn.cluster import KMeans

# Load your dataset
# For demonstration, we'll create a sample dataset
np.random.seed(0)
data = pd.DataFrame({
    'Profit': np.random.normal(loc=200, scale=50, size=100),
    'Month': np.arange(1, 101),
    'Sales': np.random.normal(loc=500, scale=100, size=100)
})

# Display the first few rows of the dataset
print("Dataset Preview:")
print(data.head())

# Choose a model based on purpose
# Purpose: Time Series Analysis for forecasting future profits
# Here, we're using linear regression as a simple model for demonstration

# Simple Linear Regression
X = data['Month']
y = data['Profit']

# Add a constant to the independent variable (Month)
X = sm.add_constant(X)

# Fit the model
model = sm.OLS(y, X).fit()

# Summary of the regression model
print("\nSimple Linear Regression Results:")
print(model.summary())

# Plotting the regression line
plt.figure(figsize=(10, 6))
plt.scatter(data['Month'], data['Profit'], label='Data Points', color='blue')
plt.plot(data['Month'], model.predict(X), label='Regression Line', color='red')
plt.title('Simple Linear Regression')
plt.xlabel('Month')
plt.ylabel('Profit')
plt.legend()
plt.show()

# Assessing variable requirements for Cluster Analysis
# For clustering, we'll use the 'Sales' and 'Profit' columns
X_cluster = data[['Sales', 'Profit']]

# K-Means Clustering
kmeans = KMeans(n_clusters=3, random_state=0)
data['Cluster'] = kmeans.fit_predict(X_cluster)

# Plotting Clusters
plt.figure(figsize=(10, 6))
plt.scatter(data['Sales'], data['Profit'], c=data['Cluster'], cmap='viridis', marker='o')
plt.title('K-Means Clustering')
plt.xlabel('Sales')
plt.ylabel('Profit')
plt.colorbar(label='Cluster')
plt.show()

# Checking assumptions for Simple Linear Regression
# Normality assumption can be checked using a Q-Q plot
sm.qqplot(model.resid, line='s')
plt.title('Q-Q Plot for Normality Check')
plt.show()

# Conducting a Shapiro-Wilk test for normality
from scipy.stats import shapiro

stat, p_value = shapiro(model.resid)
print(f"\nShapiro-Wilk Test Statistic: {stat}, p-value: {p_value}")

# Conclusion based on the p-value
alpha = 0.05
if p_value > alpha:
    print("The residuals are normally distributed (fail to reject H0)")
else:
    print("The residuals are not normally distributed (reject H0)")

# Final Notes
print("\nModeling Summary:")
print("1. Purpose: Linear Regression used for forecasting profits.")
print("2. Variable Requirements: Quantitative variables used for regression and clustering.")
print("3. Data Assumptions: Checked normality of residuals for regression.")
