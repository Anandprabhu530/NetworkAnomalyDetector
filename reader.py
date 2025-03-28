import os
import time
import json
import smtplib
from dotenv import load_dotenv
from email.mime.text import MIMEText

load_dotenv()

file_name = os.getenv("FILE_NAME")

# Have a record to keep track of the unauthorized device
# To send email only once for a unauthorized device
records = []

# Configure your Email format
subject = "Unauthorized Device"
sender = os.getenv("EMAIL_ADDRESS")
password = os.getenv("EMAIL_PASSWORD")
recipient = os.getenv("RECIPIENTS")
recipients = [sender, recipient]

def sendEmail(subject, body, sender, recipients):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender
    msg["To"] = ", ".join(recipients)
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:
        smtp_server.login(sender, password)
        smtp_server.sendmail(sender, recipients, msg=msg.as_string())


file = open(file_name,"r")

# Read the files's last line continuously
# Sleep for one second to prevent overload
while 1:
    where = file.tell()
    line = file.readline()
    if not line:
        time.sleep(1)
        file.seek(where)
    else:
        sourceAddress = json.loads(line)
        source = sourceAddress['source'].strip()
        if source not in records:
            body = "Unauthorized Device Detected \n Mac Address: " + source
            records.append(source)
            sendEmail(subject, body, sender, recipients)
