# big_data_management_systems_roundup.py

# This script provides an overview of various big data management systems.
# It highlights the pros and cons of each system, making it easier for users to understand their features and use cases.

# HBase (Distributed NoSQL Database)
# HBase is a distributed, column-oriented database built on top of the Hadoop Distributed File System (HDFS).
# It handles massive amounts of sparse, semi-structured data with real-time read/write access.

def hbase():
    # Pros of HBase
    pros = [
        "Scalable: Easily able to add new storage through a distributed structure.",
        "Fault-tolerant: A distributed database enables multiple copies to avoid data loss."
    ]
    
    # Cons of HBase
    cons = [
        "Real-time focused: Not suitable for complex transactions due to real-time processing.",
        "Complexity: Requires knowledge of HDFS and the Hadoop ecosystem."
    ]
    
    # Resource for HBase
    resource = "HBase Reference Guide"
    
    # Print information
    print("HBase:")
    print("Pros:", pros)
    print("Cons:", cons)
    print("Resource:", resource)

# Cassandra (Wide-Column Store)
# Cassandra is a distributed database designed for high availability and scalability.
# It excels in handling time-series data, IoT applications, and systems with vast amounts of data.

def cassandra():
    # Pros of Cassandra
    pros = [
        "High availability: Ensures continuous operation during server failures by replicating data.",
        "Scalability: Handles massive datasets and many simultaneous writes.",
        "Flexible partitioning: Data can be partitioned based on specific criteria."
    ]
    
    # Cons of Cassandra
    cons = [
        "Complexity: Managing a distributed database is challenging.",
        "Limited querying: Querying capabilities may not be as advanced as MongoDB."
    ]
    
    # Resource for Cassandra
    resource = "Cassandra Documentation"
    
    # Print information
    print("\nCassandra:")
    print("Pros:", pros)
    print("Cons:", cons)
    print("Resource:", resource)

# HDFS (Hadoop Distributed File System)
# HDFS is a distributed file system designed for storing large datasets across clusters of commodity hardware.
# It's used as the foundation for Big Data technologies like MapReduce, Hive, and HBase.

def hdfs():
    # Pros of HDFS
    pros = [
        "Scalable: Easily add new storage via distributed structure.",
        "Fault-tolerant: Multiple copies to prevent data loss.",
        "High throughput: Suitable for processing large files with parallelism."
    ]
    
    # Cons of HDFS
    cons = [
        "Batch processing: Not suitable for low-latency access or small files.",
        "Tool dependency: Often used as a foundation for other Big Data tools like MapReduce."
    ]
    
    # Resource for HDFS
    resource = "HDFS Architecture Guide"
    
    # Print information
    print("\nHDFS:")
    print("Pros:", pros)
    print("Cons:", cons)
    print("Resource:", resource)

# MapReduce (Programming Model)
# MapReduce is a programming model for processing large datasets in parallel across a cluster of machines.
# It simplifies distributed application development by dividing tasks into smaller sub-tasks.

def mapreduce():
    # Pros of MapReduce
    pros = [
        "Scalable: New storage can be added easily in distributed environments.",
        "Fault-tolerant: Works with distributed databases to avoid data loss."
    ]
    
    # Cons of MapReduce
    cons = [
        "Batch processing: Not ideal for low-latency or small-file processing."
    ]
    
    # Print information
    print("\nMapReduce:")
    print("Pros:", pros)
    print("Cons:", cons)

# Main function to run the overview of big data systems
def main():
    # Print a header for the script
    print("Big Data Management Systems Roundup")
    
    # Call each function to display the system overview
    hbase()
    cassandra()
    hdfs()
    mapreduce()

# Run the main function
if __name__ == "__main__":
    main()
