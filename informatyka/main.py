#!/usr/local/bin/python3

import json
import getpass
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import send_mail
from config_parser import config
from get_filename import get_filename

try:
    password = config["password"]
except KeyError:
    password = getpass.getpass(prompt="Your email password: ")

# Initialize new message
message = MIMEMultipart()
message["From"] = config["sender_email"]
message["To"] = config["receiver_email"]
message["Subject"] = config["message_subject"]

# Add body to email
message.attach(MIMEText(config["message_body"], "plain"))

filename = get_filename() + ".zip"  # In same directory as script

# Open PDF file in binary mode
with open(filename, "rb") as attachment:
    # Add file as application/octet-stream
    # Email client can usually download this automatically as attachment
    part = MIMEBase("application", "octet-stream")
    part.set_payload(attachment.read())

# Encode file in ASCII characters to send by email
encoders.encode_base64(part)

# Add header as key/value pair to attachment part
part.add_header("Content-Disposition", f"attachment; filename= {filename}")

# Add attachment to message and convert message to string
message.attach(part)
text = message.as_string()

mail = (
    text,
    config["receiver_email"],
    config["sender_email"],
    password,
    config["message_server"],
    config["message_port"]
)

if config["message_protocol"] == "ssl":
    send_mail.send_mail_ssl(*mail)
elif config["message_protocol"] == "tls":
    send_mail.send_mail_tls(*mail)
else:
    raise Exception(
        "Cannot recognize value of 'message_protocol' in config.json")
