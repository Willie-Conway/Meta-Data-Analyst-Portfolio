import pandas as pd
import cryptography
from cryptography.fernet import Fernet

# Step 1: Generate encryption key
key = Fernet.generate_key()
cipher = Fernet(key)

# Step 2: Data ingestion (from CSV)
data = pd.read_csv(r'C:\Users\hirew\OneDrive\Desktop\Meta-Data-Analyst\Python Data Analytics/customer_data.csv')


# Step 3: Encrypt sensitive data
def encrypt_data(value):
    return cipher.encrypt(value.encode()).decode()

data['encrypted_email'] = data['email'].apply(encrypt_data)
data.drop('email', axis=1, inplace=True)  # Remove the original column

# Step 4: Store encrypted data securely (e.g., in a database or file)
data.to_csv('encrypted_customer_data.csv', index=False)

# Step 5: Monitoring (simulated, in practice use logging frameworks)
print("Data processed and encrypted. Key needs to be stored securely!")

# Step 6: Secure deletion example
def secure_delete(filename):
    import os
    os.remove(filename)

# Example usage: secure_delete('customer_data.csv')
