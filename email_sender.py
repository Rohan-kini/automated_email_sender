import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

# Email template 
# Subject: Inquiry Regarding Software Development Internship Opportunities
email_template =  """Dear {company_name},

I hope this email finds you well. I am currently a third-year engineering student pursuing a B.Tech degree in Computer Engineering and am eager to explore internship opportunities in the field. I am particularly interested in roles that allow me to apply my skills in front-end and back-end development, machine learning, and database management.

I've attached my resume for your consideration. I would greatly appreciate any information you can provide about internship opportunities at {company_name} and how I may contribute to your team.

Thank you for your time and consideration. I look forward to hearing from you soon.

Best regards,
[Your Name]
[Your Phone Number]
"""


# List of recipients
recipients = [
     {"company_name": "Cognizant", "recipient_email": "doe.samunuel@cognizant.com"},
    {"company_name": "Clover Infotech", "recipient_email": "rsrp.gupta@cloveriottichtech.com"},
    #the above emails are dummy and not hold any true value
    #add more recipients....
     
]
# Resume path
resume_path = r"YOUR_RESUME_PATH"

# Email sending function
def send_email(company_name, recipient_email, resume_path):
    message = MIMEMultipart()
    message["From"] = "YOUR_EMAIL"
    message["To"] = recipient_email
    message["Subject"] = "Inquiry Regarding Software Development Internship Opportunities"

    body = email_template.format(company_name=company_name)
    message.attach(MIMEText(body, "plain"))
    
     # Extract filename from path
    filename = os.path.basename(resume_path)

    # Attach resume
    with open(resume_path, "rb") as attachment:
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())
    encoders.encode_base64(part)
    part.add_header("Content-Disposition", f"attachment; filename= {filename}")
    message.attach(part)

    server = smtplib.SMTP("smtp.gmail.com", 587)  # Change to your SMTP server and port
    server.starttls()
    server.login("YOUR_EMAIL", "YOUR_APP_PASSWORD")  # Replace with your email credentials
    text = message.as_string()
    server.sendmail("YOUR_EMAIL", recipient_email, text)
    server.quit()

# Sending emails
for recipient in recipients:
    send_email(recipient["company_name"], recipient["recipient_email"], resume_path)
