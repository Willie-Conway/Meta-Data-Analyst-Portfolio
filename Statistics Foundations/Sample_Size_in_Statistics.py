# Sample Size in Statistics

# Import necessary libraries
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Set the style for seaborn
sns.set(style="whitegrid")

# Function to generate a non-normally distributed population
def generate_population(size):
    # Generating a population with a skewed distribution (Exponential distribution)
    population = np.random.exponential(scale=2.0, size=size)
    return population

# Function to take random samples and calculate their means
def sample_means(population, sample_size, num_samples):
    means = []
    for _ in range(num_samples):
        sample = np.random.choice(population, size=sample_size, replace=False)
        means.append(np.mean(sample))
    return means

# Parameters
population_size = 10000  # Size of the population
sample_size = 30         # Size of each sample
num_samples = 1000       # Number of samples to take

# Generate the population
population = generate_population(population_size)

# Get the sample means
means = sample_means(population, sample_size, num_samples)

# Plotting the population distribution
plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
sns.histplot(population, bins=30, kde=True, color='skyblue')
plt.title('Population Distribution (Exponential)')
plt.xlabel('Value')
plt.ylabel('Frequency')

# Plotting the distribution of sample means
plt.subplot(1, 2, 2)
sns.histplot(means, bins=30, kde=True, color='salmon')
plt.title('Distribution of Sample Means')
plt.xlabel('Sample Mean')
plt.ylabel('Frequency')

# Show the plots
plt.tight_layout()
plt.show()

# Displaying means and theoretical normal distribution
mean_of_population = np.mean(population)
std_dev_of_population = np.std(population)

# Calculate the mean and standard deviation of the sample means
mean_of_sample_means = np.mean(means)
std_dev_of_sample_means = np.std(means)

print(f"Mean of Population: {mean_of_population:.2f}")
print(f"Standard Deviation of Population: {std_dev_of_population:.2f}")
print(f"Mean of Sample Means: {mean_of_sample_means:.2f}")
print(f"Standard Deviation of Sample Means: {std_dev_of_sample_means:.2f}")
