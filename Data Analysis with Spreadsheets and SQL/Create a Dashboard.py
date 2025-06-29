import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
file_path = 'Week 5 Activity Dataset - DA.C2.M3.L3.A+.csv'
df = pd.read_csv(file_path)

# Data Cleaning & Preparation
df['item_cost'] = df['item_cost'].str.replace('$', '').astype(float)
df['taxes'] = df['taxes'].str.replace('$', '').astype(float)
df['shipping'] = df['shipping'].str.replace('$', '').astype(float)
df['total_sales'] = df['item_cost'] + df['taxes'] + df['shipping']
df['transaction_date'] = pd.to_datetime(df['transaction_date'])
df['month'] = df['transaction_date'].dt.to_period('M')

# For scatter plot - Extract hour of day from transaction_date (assuming time is included; if not, simulate)
# Since time is not provided, let's randomly assign transaction times for demo purposes (or extract hour if available)
# But your dataset only shows dates, so let's simulate times here:

import numpy as np
np.random.seed(0)
df['transaction_hour'] = np.random.randint(8, 20, size=len(df))  # Simulate business hours 8 AM to 8 PM

# Quantity column doesn't exist explicitly in your dataset example, so let's assume each row = 1 quantity sold.
# Or if Quantity exists in your full dataset, replace this with actual quantity
df['quantity'] = 1  # Assumed quantity = 1 per row

# 1. Total sales by store location (Bar chart)
sales_by_location = df.groupby('store_location')['total_sales'].sum().reset_index().sort_values('total_sales', ascending=False)

# 2. Number of sales by item category (Pie chart)
sales_by_category = df['item_category'].value_counts().reset_index()
sales_by_category.columns = ['item_category', 'count']

# 3. Monthly sales trend (Line chart)
monthly_sales = df.groupby('month')['total_sales'].sum().reset_index()
monthly_sales['month'] = monthly_sales['month'].dt.to_timestamp()

# 4. Total taxes collected by store location (Bar chart)
taxes_by_location = df.groupby('store_location')['taxes'].sum().reset_index().sort_values('taxes', ascending=False)

# 5. Scatter plot: quantity ordered vs. transaction hour
scatter_data = df.groupby('transaction_hour')['quantity'].sum().reset_index()

# Set seaborn style
sns.set(style="whitegrid")

# Create dashboard with 5 charts (2 rows x 3 columns)
fig, axs = plt.subplots(2, 3, figsize=(22, 14))
fig.suptitle('BrightThreads Sales Dashboard', fontsize=22, y=1.03)

# Chart 1: Bar chart - Total sales by store location
sns.barplot(data=sales_by_location, x='store_location', y='total_sales', palette='Blues_d', ax=axs[0, 0])
axs[0, 0].set_title('Total Sales by Store Location')
axs[0, 0].set_xlabel('Store Location')
axs[0, 0].set_ylabel('Total Sales ($)')
axs[0, 0].tick_params(axis='x', rotation=45)

# Chart 2: Pie chart - Number of sales by item category
axs[0, 1].pie(sales_by_category['count'], labels=sales_by_category['item_category'], autopct='%1.1f%%', startangle=140, colors=plt.cm.Paired.colors)
axs[0, 1].set_title('Sales Distribution by Item Category')

# Chart 3: Line chart - Monthly sales trend
sns.lineplot(data=monthly_sales, x='month', y='total_sales', marker='o', color='purple', ax=axs[0, 2])
axs[0, 2].set_title('Monthly Sales Trend')
axs[0, 2].set_xlabel('Month')
axs[0, 2].set_ylabel('Total Sales ($)')
axs[0, 2].tick_params(axis='x', rotation=45)

# Chart 4: Bar chart - Total taxes collected by store location
sns.barplot(data=taxes_by_location, x='store_location', y='taxes', palette='Reds_d', ax=axs[1, 0])
axs[1, 0].set_title('Total Taxes by Store Location')
axs[1, 0].set_xlabel('Store Location')
axs[1, 0].set_ylabel('Total Taxes ($)')
axs[1, 0].tick_params(axis='x', rotation=45)

# Chart 5: Scatter plot - Quantity ordered vs. Transaction Hour
sns.scatterplot(data=scatter_data, x='transaction_hour', y='quantity', s=100, color='green', ax=axs[1, 1])
axs[1, 1].set_title('Quantity Ordered vs. Transaction Hour')
axs[1, 1].set_xlabel('Hour of Day')
axs[1, 1].set_ylabel('Quantity Ordered')
axs[1, 1].set_xticks(range(7, 21))  # Show hours from 7 AM to 8 PM approx.

# Remove last empty subplot for cleaner look
fig.delaxes(axs[1, 2])

plt.tight_layout()
plt.show()
