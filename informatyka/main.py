import email
import smtplib
import ssl
import json
import keyring
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import config

password = keyring.get_password("system", config.sender_email)

# Initialize new message
message = MIMEMultipart()
message["From"] = config.sender_email
message["To"] = config.receiver_email
message["Subject"] = config.message_subject

# Add body to email
message.attach(MIMEText(config.message_body, "plain"))

filename = "inf.zip"  # In same directory as script

# Open PDF file in binary mode
with open(filename, "rb") as attachment:
    # Add file as application/octet-stream
    # Email client can usually download this automatically as attachment
    part = MIMEBase("application", "octet-stream")
    part.set_payload(attachment.read())

# Encode file in ASCII characters to send by email    
encoders.encode_base64(part)

# Add header as key/value pair to attachment part
part.add_header(
    "Content-Disposition",
    f"attachment; filename= {filename}",
)

# Add attachment to message and convert message to string
message.attach(part)
text = message.as_string()

# Log in to server using secure context and send email
context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(config.sender_email, password)
    server.sendmail(config.sender_email, config.receiver_email, text)
