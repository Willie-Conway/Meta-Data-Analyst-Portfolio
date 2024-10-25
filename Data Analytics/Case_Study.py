# Discussion: Case Study

# We saw that Carlos is planning 
# for his new online subscription 
# product, and Keira is helping him.  
# Carlos asked Keira to help him select 
# 5 dog food and 5 cat food products to 
# make available to customers in the 
# subscription product.  Imagine you are 
# in Keira’s shoes.  

# Where do you think Keira might obtain 
# relevant data to help her?

# And, what are the things Keira should 
# consider when scrubbing the data? 

import pandas as pd

# Step 1: Gather Data
def gather_data():
    try:
        market_research_data = pd.read_csv(r'C:/Users/hirew/OneDrive/Desktop/Meta-Data-Analyst/CSV/market_research.csv')
        online_retail_data = pd.read_csv(r'C:/Users/hirew/OneDrive/Desktop/Meta-Data-Analyst/CSV/online_retail.csv')
        social_media_data = pd.read_csv(r'C:/Users/hirew/OneDrive/Desktop/Meta-Data-Analyst/CSV/social_media.csv')
    except FileNotFoundError as e:
        print(f"Error: {e}")
        return pd.DataFrame()

    combined_data = pd.concat([market_research_data, online_retail_data, social_media_data], ignore_index=True)
    print("Columns in combined data:", combined_data.columns)
    print("Combined Data:")
    print(combined_data)
    return combined_data

# Step 2: Clean and Scrub Data
def clean_data(data):
    if data.empty:
        print("No data to clean.")
        return data

    data = data.drop_duplicates()

    # Check if required columns are present
    if 'price' not in data.columns or 'category' not in data.columns:
        print("Required columns are missing from the data.")
        return data

    # Remove entries with missing values in relevant columns
    data = data.dropna(subset=['price', 'category'])

    print("Data after cleaning and before filtering:")
    print(data)

    if data.empty:
        print("No data available after initial cleaning.")
        return data

    # Filter out outliers based on price
    price_mean = data['price'].mean()
    price_std = data['price'].std()
    data = data[(data['price'] >= price_mean - 3 * price_std) & (data['price'] <= price_mean + 3 * price_std)]

    # Check contents of category for filtering
    print("Unique categories available for filtering:", data['category'].unique())

    # Adjust relevant trends based on actual data
    relevant_categories = ['Electronics', 'Furniture', 'Home Appliances']
    data = data[data['category'].isin(relevant_categories)]

    return data

# Step 3: Analyze Data
def analyze_data(cleaned_data):
    if cleaned_data.empty:
        print("No data to analyze.")
        return pd.DataFrame()

    summary = cleaned_data.groupby('category').agg({'quantity': 'sum', 'price': 'mean'}).reset_index()
    return summary

# Main function to execute the script
def main():
    raw_data = gather_data()
    cleaned_data = clean_data(raw_data)
    product_summary = analyze_data(cleaned_data)
    print(product_summary)

# Execute the script
if __name__ == "__main__":
    main()
