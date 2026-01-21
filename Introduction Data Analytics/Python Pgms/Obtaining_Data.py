import pandas as pd
import random

# Function to generate synthetic dog food data
def generate_dog_food_data(num_products=20):
    dog_food_brands = [
        "Brand A", "Brand B", "Brand C", "Brand D", "Brand E",
        "Brand F", "Brand G", "Brand H", "Brand I", "Brand J"
    ]
    
    data = []
    for _ in range(num_products):
        brand = random.choice(dog_food_brands)
        product_name = f"{brand} Dog Food {random.randint(1, 100)}"
        price = round(random.uniform(10.0, 60.0), 2)
        rating = round(random.uniform(1.0, 5.0), 1)
        description = random.choice([
            "high protein", "grain-free", "organic", "with vegetables", "natural ingredients"
        ])
        data.append({
            "product_type": "dog",
            "brand": brand,
            "product_name": product_name,
            "price": price,
            "rating": rating,
            "description": description
        })
    return pd.DataFrame(data)

# Function to generate synthetic cat food data
def generate_cat_food_data(num_products=20):
    cat_food_brands = [
        "Brand K", "Brand L", "Brand M", "Brand N", "Brand O",
        "Brand P", "Brand Q", "Brand R", "Brand S", "Brand T"
    ]
    
    data = []
    for _ in range(num_products):
        brand = random.choice(cat_food_brands)
        product_name = f"{brand} Cat Food {random.randint(1, 100)}"
        price = round(random.uniform(10.0, 60.0), 2)
        rating = round(random.uniform(1.0, 5.0), 1)
        description = random.choice([
            "high protein", "grain-free", "organic", "with fish", "natural ingredients"
        ])
        data.append({
            "product_type": "cat",
            "brand": brand,
            "product_name": product_name,
            "price": price,
            "rating": rating,
            "description": description
        })
    return pd.DataFrame(data)

# Generate the datasets
dog_food_data = generate_dog_food_data()
cat_food_data = generate_cat_food_data()

# Combine the dog and cat food data into one DataFrame
combined_data = pd.concat([dog_food_data, cat_food_data], ignore_index=True)

# Save to CSV for further processing
combined_data.to_csv('pet_food_data.csv', index=False)

# Display the generated data
print(combined_data.head())
