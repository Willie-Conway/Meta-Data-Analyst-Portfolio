# Step 1: Define the original email from the company
original_email = """
Subject: Decision on Your Social Media Campaign Proposal

Dear Team,

I hope this email finds you well. Thank you for submitting your proposal for our upcoming social media campaign. We appreciate the time and effort your team dedicated to crafting a comprehensive and creative plan.

After careful consideration and thorough review of all the proposals we received, we regret to inform you that we have decided to move forward with another team for this project. This decision was not easy, as we received many excellent proposals, including yours.

Thank you once again for your participation and understanding. We wish you all the best in your future endeavors and look forward to potentially collaborating with you in the future.

Best regards,

Company
"""

# Step 2: Generate the email response
def generate_email_response(original_email):
    response = f"""
Subject: Re: Decision on Your Social Media Campaign Proposal

Dear [Company Name/Contact Name],

Thank you for your email and for the opportunity to submit our proposal for the upcoming social media campaign. While we are disappointed to hear that we were not selected, we truly appreciate the consideration given to our proposal.

To help us improve our future submissions, could you please provide some feedback on why our proposal was not chosen? Any insights you could share would be invaluable to us as we strive to enhance our offerings.

We genuinely value the possibility of collaborating with your team in the future and hope to stay in touch for any upcoming projects.

Thank you once again for your time and consideration. We wish you the best of luck with your campaign and look forward to the potential for future opportunities.

Best regards,

Willie Conway
Data Analyst at Meta
hire.willie.conway@gmail.com
"""
    return response

# Step 3: Output the original email and the generated response
print("Original Email:")
print(original_email)
print("\nGenerated Response:")
print(generate_email_response(original_email))
