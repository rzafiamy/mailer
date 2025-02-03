import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import argparse
from config import SENDER_EMAIL, SENDER_PASSWORD, SMTP_SERVER, SMTP_PORT

# Define command-line arguments
parser = argparse.ArgumentParser(description='Send an email using SMTP.')
parser.add_argument('--sender', type=str, default=SENDER_EMAIL, help='Sender email address')
parser.add_argument('--recipient', type=str, required=True, help='Recipient email address')
parser.add_argument('--subject', type=str, required=True, help='Subject of the email')
parser.add_argument('--body', type=str, required=True, help='Body of the email')

args = parser.parse_args()

# Create the email
msg = MIMEMultipart()
msg['From'] = args.sender
msg['To'] = args.recipient
msg['Subject'] = args.subject
msg.attach(MIMEText(args.body, 'plain'))

# Send the email
try:
    # Use SMTP_SSL for a secure connection
    server = smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT)
    server.login(SENDER_EMAIL, SENDER_PASSWORD)
    server.sendmail(args.sender, args.recipient, msg.as_string())
    server.quit()
    print("Email sent successfully!")
except Exception as e:
    print(f"Failed to send email: {e}")
