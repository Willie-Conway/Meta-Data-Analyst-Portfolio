# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.holtwinters import ExponentialSmoothing
from statsmodels.tsa.stattools import adfuller

# Sample time series data creation: Monthly website visits from Jan 2015 to Dec 2020
# Here we define a time series dataset with a date range and simulated visits
date_rng = pd.date_range(start='2015-01-01', end='2020-12-31', freq='M')  # Monthly frequency
np.random.seed(0)  # For reproducibility

# Simulating time series data: Poisson distribution for website visits with an increasing trend
website_visits = np.random.poisson(lam=1000, size=len(date_rng)) + np.arange(len(date_rng)) * 10  # Simulated growth

# Create a DataFrame to hold the time series data
data = pd.DataFrame(data={'date': date_rng, 'website_visits': website_visits})
data.set_index('date', inplace=True)  # Set date as the index for time series analysis

# Display the first few rows of the time series dataset
print(data.head())

# Plot the original time series data
plt.figure(figsize=(12, 6))
plt.plot(data.index, data['website_visits'], label='Website Visits', color='blue')
plt.title('Monthly Website Visits Time Series (Jan 2015 - Dec 2020)')
plt.xlabel('Date')
plt.ylabel('Number of Visits')
plt.legend()
plt.grid()
plt.show()

# Check for stationarity of the time series data using the ADF test
result = adfuller(data['website_visits'])
print('ADF Statistic:', result[0])
print('p-value:', result[1])

# If the p-value is above 0.05, the series is non-stationary
if result[1] > 0.05:
    print("The time series is non-stationary; differencing may be needed.")
    data['website_visits_diff'] = data['website_visits'].diff()
    data.dropna(inplace=True)  # Drop the NaN values from differencing

    # Plot the differenced time series data to check for stationarity
    plt.figure(figsize=(12, 6))
    plt.plot(data.index, data['website_visits_diff'], label='Differenced Website Visits', color='orange')
    plt.title('Differenced Monthly Website Visits Time Series')
    plt.xlabel('Date')
    plt.ylabel('Differenced Visits')
    plt.legend()
    plt.grid()
    plt.show()

# Fit a time series model: Using Exponential Smoothing for forecasting
model = ExponentialSmoothing(data['website_visits'], trend='add', seasonal=None, seasonal_periods=12)
fit = model.fit()

# Forecast the next 12 months based on the time series data
forecast = fit.forecast(steps=12)

# Plotting the historical time series data and the forecast
plt.figure(figsize=(12, 6))
plt.plot(data.index, data['website_visits'], label='Historical Data', color='blue')
plt.plot(forecast.index, forecast, label='Forecast', color='red', linestyle='--')
plt.title('Website Visits Forecast for the Next Year (Time Series Analysis)')
plt.xlabel('Date')
plt.ylabel('Number of Visits')
plt.legend()
plt.grid()
plt.show()

# Display forecasted values
print("Forecasted Website Visits for the next 12 months:")
print(forecast)
