# storage_tools_roundup.py

# This script provides an overview of cloud-based storage tools and their features,
# focusing on various popular cloud platforms and big data solutions.

# Cloud Storage Tools Overview
# Cloud storage allows offsite data saving with access via network connections (e.g., the Internet).
# Cloud-based storage offers secure, scalable, and cost-effective ways to manage data.

# Amazon Web Services (AWS)
# AWS offers Amazon Simple Storage Service (S3), a scalable and secure object storage service.
# Object storage manages data as discrete units called objects, each with its own identifier and metadata.

def aws_storage():
    # Description of AWS S3
    description = "Amazon S3 is a scalable object storage service, ideal for data lakes, backups, and content distribution."
    
    # Resource for AWS
    resource = "AWS Storage Overview: https://aws.amazon.com/products/storage/"
    
    # Print information about AWS S3
    print("Amazon Web Services (AWS):")
    print("Description:", description)
    print("Resource:", resource)

# Azure Storage
# Azure offers Azure Blob storage, which is a scalable object storage solution for various data types.
# It's similar to AWS in scalability and pricing, with integration into other Microsoft products.

def azure_storage():
    # Description of Azure Blob Storage
    description = "Azure Blob storage is a scalable object storage service, ideal for unstructured data and backups."
    
    # Resource for Azure
    resource = "Azure Storage Overview: https://azure.microsoft.com/en-us/services/storage/"
    
    # Print information about Azure Blob Storage
    print("\nAzure:")
    print("Description:", description)
    print("Resource:", resource)

# Google Cloud Platform (GCP)
# GCP provides Cloud Storage, which is designed to store and retrieve any data at any time.
# It offers several storage classes like Standard, Nearline, Coldline, and Archive.

def gcp_storage():
    # Description of Google Cloud Storage
    description = "Google Cloud Storage supports multiple storage classes and is ideal for unstructured data, backups, and large-scale processing."
    
    # Resource for GCP
    resource = "Cloud Storage Overview: https://cloud.google.com/storage"
    
    # Print information about GCP Cloud Storage
    print("\nGoogle Cloud Platform (GCP):")
    print("Description:", description)
    print("Resource:", resource)

# Apache Spark
# Apache Spark is an open-source framework primarily used for fast, in-memory data processing.
# Spark can interact with various data sources such as HDFS, Amazon S3, and JDBC.

def apache_spark():
    # Description of Apache Spark
    description = "Apache Spark is a framework for in-memory data processing, capable of reading from multiple data sources like HDFS and S3."
    
    # Resource for Apache Spark
    resource = "Apache Spark Overview: https://spark.apache.org/"
    
    # Print information about Apache Spark
    print("\nApache Spark:")
    print("Description:", description)
    print("Resource:", resource)

# Apache Hadoop
# Hadoop is an open-source framework designed for large-scale data storage and processing.
# The core storage component, Hadoop Distributed File System (HDFS), distributes data across multiple nodes for high throughput.

def apache_hadoop():
    # Description of Apache Hadoop
    description = "Apache Hadoop provides scalable storage with its Hadoop Distributed File System (HDFS), ideal for large datasets."
    
    # Resource for Apache Hadoop
    resource = "Hadoop Overview: https://hadoop.apache.org/"
    
    # Print information about Apache Hadoop
    print("\nApache Hadoop:")
    print("Description:", description)
    print("Resource:", resource)

# Main function to run the overview of storage tools
def main():
    # Print a header for the script
    print("Storage Tools Roundup")
    
    # Call each function to display the overview of cloud and big data storage systems
    aws_storage()
    azure_storage()
    gcp_storage()
    apache_spark()
    apache_hadoop()

# Run the main function
if __name__ == "__main__":
    main()
