# Different Types Of Models

# Import necessary libraries
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.cluster import KMeans
from sklearn.metrics import mean_squared_error, accuracy_score
from sklearn.neural_network import MLPClassifier
import matplotlib.pyplot as plt

# Generate synthetic data for demonstration
# Regression dataset
np.random.seed(42)
X_reg = np.random.rand(100, 1) * 10  # 100 samples, 1 feature
y_reg = 2.5 * X_reg + np.random.randn(100, 1) * 2  # Linear relationship with noise

# Classification dataset
X_clf = np.random.rand(100, 2)  # 100 samples, 2 features
y_clf = (X_clf[:, 0] + X_clf[:, 1] > 1).astype(int)  # Binary classification based on sum of features

# Clustering dataset
X_clu = np.random.rand(100, 2)  # 100 samples, 2 features for clustering

# 1. Regression Model
def regression_model(X, y):
    # Split the dataset into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Create and train the Linear Regression model
    model = LinearRegression()
    model.fit(X_train, y_train)
    
    # Predict on the test set
    y_pred = model.predict(X_test)
    
    # Calculate and print the Mean Squared Error
    mse = mean_squared_error(y_test, y_pred)
    print(f"Regression Mean Squared Error: {mse:.2f}")
    
    # Plotting the results
    plt.scatter(X_test, y_test, color='blue', label='Actual')
    plt.scatter(X_test, y_pred, color='red', label='Predicted')
    plt.title('Regression Model Predictions')
    plt.xlabel('Feature')
    plt.ylabel('Target')
    plt.legend()
    plt.show()

# 2. Decision Tree Model
def decision_tree_model(X, y):
    # Split the dataset into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Create and train the Decision Tree Classifier
    model = DecisionTreeClassifier(random_state=42)
    model.fit(X_train, y_train)
    
    # Predict on the test set
    y_pred = model.predict(X_test)
    
    # Calculate and print the accuracy
    accuracy = accuracy_score(y_test, y_pred)
    print(f"Decision Tree Classification Accuracy: {accuracy:.2f}")

# 3. Neural Network Model
def neural_network_model(X, y):
    # Split the dataset into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Create and train the Neural Network Classifier
    model = MLPClassifier(hidden_layer_sizes=(5,), max_iter=1000, random_state=42)
    model.fit(X_train, y_train)
    
    # Predict on the test set
    y_pred = model.predict(X_test)
    
    # Calculate and print the accuracy
    accuracy = accuracy_score(y_test, y_pred)
    print(f"Neural Network Classification Accuracy: {accuracy:.2f}")

# 4. Clustering Algorithm
def clustering_model(X):
    # Create and fit the KMeans model
    model = KMeans(n_clusters=3, random_state=42)
    model.fit(X)
    
    # Predict clusters
    clusters = model.predict(X)
    
    # Plotting the clusters
    plt.scatter(X[:, 0], X[:, 1], c=clusters, cmap='viridis')
    plt.title('K-Means Clustering')
    plt.xlabel('Feature 1')
    plt.ylabel('Feature 2')
    plt.show()

# Run the models
print("Running Regression Model...")
regression_model(X_reg, y_reg)

print("\nRunning Decision Tree Model...")
decision_tree_model(X_clf, y_clf)

print("\nRunning Neural Network Model...")
neural_network_model(X_clf, y_clf)

print("\nRunning Clustering Model...")
clustering_model(X_clu)
