"""
Compliance Best Practices Guide
This script outlines best practices for data compliance, governance, and security.
"""

# Data Compliance
def data_compliance_overview():
    """
    Data compliance involves adhering to regulations and standards 
    that govern data management, ensuring organizations minimize risks 
    and foster trust with users and stakeholders.
    """
    print("Data Compliance Overview:")
    print("Data compliance is crucial for organizations to adhere to legal requirements and industry standards, "
          "thereby protecting sensitive information and building trust with users.")
    print("Key Regulations: GDPR, CCPA, HIPAA.\n")


# Data Governance
def data_governance():
    """
    Data Governance establishes internal rules for data ownership and accountability.
    
    Components:
        - Data classification schemes
        - Development of data privacy policies
        - Appointment of a data governance team
    
    Analogy: Organizing warehouse shelves to create clear rules for 
    data categorization, protection, and usage.
    """
    print("Data Governance:")
    print("Data governance involves defining who can take what actions with what data, and under what circumstances.")
    print("It ensures data is accurate, available, and secure.")
    print("Components include data classification, privacy policies, and governance teams.\n")


# Data Security
def data_security():
    """
    Data Security protects data from unauthorized access, breaches, and loss.
    
    Methods:
        - Implementing security measures like encryption, firewalls, 
          and intrusion detection systems.
    """
    print("Data Security:")
    print("Data security encompasses all measures to protect data from unauthorized access and breaches.")
    print("Methods include encryption, firewalls, intrusion detection, and secure access protocols.\n")


# Access Controls
def access_controls():
    """
    Access Controls restrict who can access and modify data.
    
    Approach: Role-Based Access Control (RBAC) grants access based 
    on user roles and responsibilities.
    """
    print("Access Controls:")
    print("Access controls ensure that only authorized users can access or modify data.")
    print("Role-Based Access Control (RBAC) assigns permissions based on user roles, enhancing security and accountability.\n")


# Data Breach Response
def data_breach_response():
    """
    Data Breach Response prepares organizations for effective 
    responses to data security incidents.
    
    Components:
        - Data breach response plan
        - Dedicated incident management team
        - Clear communication protocols
    """
    print("Data Breach Response:")
    print("Organizations must have a response plan for data breaches to minimize damage.")
    print("Components include a dedicated team, clear communication strategies, and a step-by-step response plan.\n")


# Data Anonymization and Pseudonymization
def data_anonymization_and_pseudonymization():
    """
    Anonymization: Irreversibly transforms data to prevent linkage 
    to individuals (e.g., removing logos from beverage cans). 
    Not considered personal data under regulations like GDPR.
    
    Pseudonymization: Replaces identifying information with aliases 
    while allowing potential re-identification (e.g., using codes like ID#456). 
    Risk of re-identification exists if linking keys are compromised.
    """
    print("Data Anonymization and Pseudonymization:")
    print("Anonymization makes data untraceable to individuals, providing a level of privacy.")
    print("Pseudonymization allows data to be linked back to individuals under certain conditions, "
          "but it poses risks if identifiers are compromised.\n")


# Choosing Between Anonymization and Pseudonymization
def choose_between_methods():
    """
    Use Cases:
        - Anonymized data is ideal for scenarios where individual 
          identities are irrelevant (e.g., music listening trends).
        - Pseudonymized data is suitable when some identification is needed 
          (e.g., informing study participants of results).
    """
    print("Choosing Between Anonymization and Pseudonymization:")
    print("Anonymization is preferred for analysis where individual identities are not needed.")
    print("Pseudonymization is suitable when you need to re-identify subjects later, "
          "for example in clinical trials or user research.\n")


# Data Privacy Regulations
def data_privacy_regulations():
    """
    Overview of prominent data privacy regulations:
    
    1. GDPR (General Data Protection Regulation):
       - EU law ensuring online information safety.
       - Key rights include:
           - Right to know
           - Right to edit
           - Right to be forgotten
           - Right to data portability
       - Significant fines for non-compliance (up to 4% of annual earnings).
    
    2. CCPA (California Consumer Privacy Act):
       - Provides California residents with rights similar to GDPR.
       - Key rights include:
           - Right to know data collected
           - Right to opt-out of data sales
           - Right to request deletion of data
       - Enforcement by the California attorney general with fines ranging from 
         $2500 to $7500.
    
    3. COPPA (Children's Online Privacy Protection Act):
       - Protects children's data in the U.S.
       - Requirements include:
           - Extra verification for collecting data from children under 13
           - Clear data collection disclosures
           - Parental permission before data collection
           - Ensured security of collected data
       - Enforced by the FTC with fines up to $50,000 per violation.
    """
    print("Data Privacy Regulations:")
    print("1. GDPR: Protects EU citizens' data, imposing strict regulations on data usage.")
    print("2. CCPA: Grants rights to California residents similar to GDPR.")
    print("3. COPPA: Focuses on protecting children's data in the U.S., requiring parental consent.\n")


if __name__ == "__main__":
    # Entry point for executing compliance functions
    data_compliance_overview()
    data_governance()
    data_security()
    access_controls()
    data_breach_response()
    data_anonymization_and_pseudonymization()
    choose_between_methods()
    data_privacy_regulations()
