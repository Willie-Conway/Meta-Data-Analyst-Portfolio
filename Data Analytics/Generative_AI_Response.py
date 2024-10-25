# Import necessary libraries
import random

# Function to generate a random recipient name
def generate_random_recipient():
    first_names = ["Alice", "Bob", "Charlie", "Dana", "Evelyn"]
    last_names = ["Smith", "Johnson", "Williams", "Brown", "Jones"]
    
    # Randomly select a first name and a last name to create a full name
    return f"{random.choice(first_names)} {random.choice(last_names)}"

# Function to simulate sending an email response
def send_email_response(original_email, recipient_name):
    # Create a response email
    response = f"""
    Subject: Re: Decision on Your Social Media Campaign Proposal

    Dear {recipient_name},

    Thank you for your email regarding our proposal for the social media campaign. While we are disappointed not to be selected, we truly appreciate the opportunity to submit our ideas to Meta.

    We would love to gain more insights into the decision-making process. Could you please provide feedback on our proposal? Understanding where we might improve would be incredibly helpful for our future submissions.

    Additionally, we hope there may be opportunities for collaboration in the future. We believe that our team can bring valuable ideas and creativity to Meta.

    Thank you once again for considering our proposal. We look forward to your feedback.

    Best regards,
    Willie Conway
    Data Analyst
    Meta
    hire.willie.conway@gmail.com
    """

    # Print the response email
    print(response)

# Main execution
if __name__ == "__main__":
    # Original email context (hypothetical)
    original_email = """
    Dear Team,

    I hope this email finds you well. Thank you for submitting your proposal for our upcoming social media campaign. We appreciate the time and effort your team dedicated to crafting a comprehensive and creative plan.

    After careful consideration and thorough review of all the proposals we received, we regret to inform you that we have decided to move forward with another team for this project. This decision was not easy, as we received many excellent proposals, including yours.

    Thank you once again for your participation and understanding. We wish you all the best in your future endeavors and look forward to potentially collaborating with you in the future.

    Best regards,
    Company
    """

    # Generate a random recipient name
    recipient_name = generate_random_recipient()

    # Call function to send email response
    send_email_response(original_email, recipient_name)
