

# Email Sender for Internship Inquiry

This Python script allows you to send internship/job/sending bulk certificates  emails to multiple recipients using a customized email template and attaching your resume or other relevant document.

## Features

- **Customizable Email Template**: The email template allows you to personalize the message for any subject of your choice 
- **Attachment Support**: You can attach your resume to each email or any other document you want to send to bulk recipients
- **Multiple Recipients**: You can specify multiple recipients along with their company names and email addresses.
- **Security**: The script does not contain any email addresses or app passwords. Users need to set up their own email credentials for sending emails.

```markdown
## Installation

1. Clone this repository:

```bash
git clone https://github.com/your-username/email-sender.git
```

2. Navigate to the project directory:

```bash
cd email-sender
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

## Configuration

1. Set up your email account:
   - Navigate to your email account settings, then access the security section. Look for the option to generate an 'app password' and create one if it's not already available. Copy the generated app password and paste it into the code where the original password of your Gmail account is requested. It's important to note that the script requires an app password, which is a unique password specifically generated for applications like this, ensuring the security of your Gmail account.
   - Replace `"YOUR_EMAIL"` and `"YOUR_APP_PASSWORD"` in the script with your email address and app password respectively.

2. Customize the email template:
   - Modify the `email_template` variable in the script to create your own email message. Generate email_template the way you wish the way you need

3. Specify recipients:
   - Add recipient details to the `recipients` list in the script. Each recipient should have a `"company_name"` and `"recipient_email"`.

4. Set the resume path:
   - Replace `"YOUR_RESUME_PATH"` with the path to your resume file.

## Usage

Run the script:

```bash
python email_sender.py
```

The script will send emails to all specified recipients hassle free.

## Note

- Ensure that your email account settings allow sending emails via SMTP. You may need to adjust security settings to enable this.
- Test the script with a small number of recipients before sending emails to a large list to avoid any issues.

```
