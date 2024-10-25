# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix

# OSEMN Framework Steps

# 1. Obtain Data
# Creating a synthetic dataset representing cat and dog products with relevant features.
data = {
    'Product': ['Cat Food', 'Dog Food', 'Cat Toy', 'Dog Toy', 'Cat Treat', 'Dog Treat'],
    'Category': ['Cat', 'Dog', 'Cat', 'Dog', 'Cat', 'Dog'],
    'Price': [10.99, 12.49, 5.99, 7.99, 4.99, 6.99],  # Price of the product
    'Rating': [4.5, 4.7, 4.3, 4.6, 4.8, 4.5],         # Customer rating of the product
    'Sales': [150, 200, 180, 160, 220, 190]            # Number of units sold
}

# Creating a DataFrame from the data dictionary
df = pd.DataFrame(data)

# Display the first few rows of the DataFrame to verify data
print("Data Sample:")
print(df)

# 2. Scrub Data
# Check for missing values in the dataset
print("\nMissing Values:")
print(df.isnull().sum())  # Outputs the count of missing values for each column

# In this example, we assume there are no missing values.
# If there were, we could handle them as needed, e.g., filling or dropping.

# 3. Explore Data
# Generate descriptive statistics to understand data distribution
print("\nDescriptive Statistics:")
print(df.describe())

# Visualize Sales vs. Rating using a bar plot
plt.figure(figsize=(10, 5))
sns.barplot(x='Product', y='Sales', hue='Category', data=df)
plt.title('Sales of Cat and Dog Products')
plt.xlabel('Product')
plt.ylabel('Sales')
plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
plt.show()

# Calculate correlation only on numeric columns (Price, Rating, Sales)
correlation = df[['Price', 'Rating', 'Sales']].corr()
print("\nCorrelation Matrix:")
print(correlation)  # Print the correlation matrix to the console

# Plotting the correlation matrix using a heatmap
plt.figure(figsize=(8, 5))
sns.heatmap(correlation, annot=True, cmap='coolwarm')
plt.title('Correlation Matrix')
plt.show()

# 4. Model
# Prepare features (X) and target (y) for modeling
X = df[['Price', 'Rating']]  # Features used for prediction
# Create a binary target variable: 1 for Dog, 0 for Cat
y = df['Category'].apply(lambda x: 1 if x == 'Dog' else 0)

# Split the dataset into training and testing sets (80% training, 20% testing)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create and train the Logistic Regression model
model = LogisticRegression()
model.fit(X_train, y_train)  # Fitting the model to the training data

# Predict the categories on the test set
y_pred = model.predict(X_test)

# 5. Interpret
# Evaluate the model's performance using a classification report
print("\nClassification Report:")
print(classification_report(y_test, y_pred))

# Generate a confusion matrix to visualize the model's predictions
cm = confusion_matrix(y_test, y_pred)
plt.figure(figsize=(5, 5))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=['Cat', 'Dog'], yticklabels=['Cat', 'Dog'])
plt.title('Confusion Matrix')
plt.ylabel('Actual')
plt.xlabel('Predicted')
plt.show()

# Conclusion
# The model can now predict whether a product is for a cat or a dog based on its features (Price and Rating).
# Further steps could involve refining the model, exploring additional features, or using more advanced algorithms.
