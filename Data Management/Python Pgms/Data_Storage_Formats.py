# Roundup of Storage Formats
# This script outlines three common data storage formats: Relational Databases,
# NoSQL Databases, and File-based Storage, along with their pros and cons.

# Function to display information about Relational Databases
def relational_database_info():
    """
    Relational Databases:
    - Enforce relationships between tables, ensuring data consistency.
    - Example: A customer record in one table linked to order records in another.
    """
    print("Relational Database:")
    print("Pros:")
    print(" - Strong data structure and organization")
    print(" - Excellent data integrity and consistency")
    print(" - Powerful querying capabilities for complex relationships")
    
    print("Cons:")
    print(" - Less flexible for unstructured data (like images or videos)")
    print(" - Scaling can be challenging for massive datasets")
    print(" - Complex queries can slow down performance")
    print()

# Function to display information about NoSQL Databases
def nosql_database_info():
    """
    NoSQL Databases:
    - Represents a category of databases with a different approach to data storage.
    - Schema-less or schema-flexible, allowing for various types of data.
    """
    print("NoSQL Database:")
    print("Pros:")
    print(" - Highly scalable for massive datasets")
    print(" - Flexible for storing unstructured data")
    print(" - Ideal for high-performance applications")
    
    print("Cons:")
    print(" - Weaker data consistency compared to relational databases")
    print(" - Complex querying capabilities might be limited")
    print(" - May require additional effort to ensure data integrity")
    print()

# Function to display information about File-based Storage
def file_based_storage_info():
    """
    File-based Storage:
    - Organizes data into individual files, resembling a digital filing cabinet.
    - Suitable for simple file sharing and management.
    """
    print("File-based Storage:")
    print("Pros:")
    print(" - Simple to use and understand")
    print(" - Easy to access and share individual files")
    print(" - Cost-effective for small to medium datasets")
    
    print("Cons:")
    print(" - Not ideal for large datasets or complex data relationships")
    print(" - Limited data security and access control features")
    print(" - Can become cumbersome to manage as data grows")
    print()

# Main function to execute the script
def main():
    relational_database_info()
    nosql_database_info()
    file_based_storage_info()

# Entry point of the script
if __name__ == "__main__":
    main()
