# data_security_fundamentals.py

# This script provides an overview of data security and data privacy fundamentals, 
# including their definitions, benefits, limitations, and key concepts.

# Data Security
def data_security():
    # Description of data security
    description = ("Data security is a critical challenge due to various threats "
                   "from malicious actors who aim to steal, corrupt, or disrupt data.")
    
    # Common security threats
    threats = [
        "Malware (viruses, ransomware) that infiltrates systems to steal or corrupt data.",
        "Phishing attacks that trick users into revealing sensitive information.",
        "Unsecured networks (e.g., public Wi-Fi) exposing data to unauthorized access.",
        "Weak passwords that can be compromised through brute-force attacks."
    ]
    
    # Defense measures against data security threats
    defenses = [
        "Data encryption to scramble data, making it useless if intercepted.",
        "Regular backups to maintain copies of data.",
        "Access controls that restrict data access based on user roles.",
        "Security awareness training to educate users about best practices.",
        "Incident response plans to minimize damage from breaches."
    ]

    # Print information about data security
    print("Data Security:")
    print("Description:", description)
    print("Common Security Threats:")
    for threat in threats:
        print(" -", threat)
    print("Defense Measures:")
    for defense in defenses:
        print(" -", defense)

# Benefits and Limitations of Data Security
def benefits_and_limitations_data_security():
    benefits = [
        "Protects against breaches and misuse.",
        "Safeguards data integrity.",
        "Builds trust in data-driven insights."
    ]
    
    limitations = [
        "Security measures can be expensive.",
        "May introduce delays in data access.",
        "Achieving absolute security is an ongoing challenge."
    ]
    
    # Print benefits and limitations of data security
    print("\nBenefits and Limitations of Data Security:")
    print("Benefits:")
    for benefit in benefits:
        print(" -", benefit)
    print("Limitations:")
    for limitation in limitations:
        print(" -", limitation)

# Data Privacy
def data_privacy():
    # Description of data privacy
    description = ("Data privacy gives individuals control over their personal information, "
                   "allowing them to decide what data is collected and how it is used.")
    
    # Print information about data privacy
    print("\nData Privacy:")
    print("Description:", description)

# Benefits and Limitations of Data Privacy
def benefits_and_limitations_data_privacy():
    benefits = [
        "Empowers individuals to control their data.",
        "Fosters trust between individuals and organizations.",
        "Reduces risks of identity theft."
    ]
    
    limitations = [
        "Balancing individual privacy with business needs can be complex.",
        "Enforcing regulations across borders is challenging.",
        "Understanding complex data usage practices can be difficult."
    ]
    
    # Print benefits and limitations of data privacy
    print("\nBenefits and Limitations of Data Privacy:")
    print("Benefits:")
    for benefit in benefits:
        print(" -", benefit)
    print("Limitations:")
    for limitation in limitations:
        print(" -", limitation)

# Security Threats and Vulnerabilities
def security_threats_and_vulnerabilities():
    threats = [
        "Malware (viruses, ransomware) that can infiltrate systems.",
        "Phishing attacks that deceive users into revealing sensitive information."
    ]
    
    vulnerabilities = [
        "Unsecured networks (like public Wi-Fi).",
        "Weak password policies."
    ]
    
    # Print information about security threats and vulnerabilities
    print("\nSecurity Threats and Vulnerabilities:")
    print("Common Threats:")
    for threat in threats:
        print(" -", threat)
    print("Vulnerabilities:")
    for vulnerability in vulnerabilities:
        print(" -", vulnerability)

# Encryption and Access Control
def encryption_and_access_control():
    # Description of encryption
    encryption_description = ("Encryption scrambles data, ensuring confidentiality and integrity. "
                               "There are two main types of encryption:")
    
    symmetric_encryption = "Symmetric encryption uses a single key for both encryption and decryption."
    asymmetric_encryption = ("Asymmetric encryption uses separate public and private keys, "
                             "ideal for secure communication.")
    
    # Access control description
    access_control_description = ("Access control restricts who can access data and what actions they can perform. "
                                   "Key components include subjects, objects, and permissions.")
    
    # Print information about encryption and access control
    print("\nEncryption and Access Control:")
    print("Encryption Description:", encryption_description)
    print("Types of Encryption:")
    print(" -", symmetric_encryption)
    print(" -", asymmetric_encryption)
    print("Access Control Description:", access_control_description)

# Main function to run the overview of data security fundamentals
def main():
    # Print a header for the script
    print("Summary: Data Security Fundamentals")
    
    # Call each function to display the overview of data security and privacy
    data_security()
    benefits_and_limitations_data_security()
    data_privacy()
    benefits_and_limitations_data_privacy()
    security_threats_and_vulnerabilities()
    encryption_and_access_control()

# Run the main function
if __name__ == "__main__":
    main()
