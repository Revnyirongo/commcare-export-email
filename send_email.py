import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
import subprocess

# Replace these values with your own email settings
sender_email = 'yoemail@mail.org'
sender_password = 'password'
recipient_email = 'rev@mail.com'

# Create the message container
msg = MIMEMultipart()
msg['From'] = sender_email
msg['To'] = recipient_email
msg['Subject'] = 'Cyclone Data'

# Run the commcare-export command to generate the Excel file
filename = 'CYC-Chikwawa-export.xlsx'
command = ['commcare-export', '--output-format', 'xlsx', '--output', filename, '--project', 'WORKSPACE-HERE', '--query',
           './query_ck.xlsx', '--username', 'username-comccar', '--auth-mode', 'apikey', '--password', 'yourAPIKeyHere']
subprocess.run(command, check=True)

# Attach the Excel file to the email
filename = 'CYC-Chikwawa-export.xlsx'
with open(filename, "rb") as f:
    attach = MIMEApplication(f.read(), _subtype="xlsx")
    attach.add_header('Content-Disposition', 'attachment',
                      filename=str(filename))
    msg.attach(attach)

# Send the email
with smtplib.SMTP('smtp.office365.com', 587) as server:
    server.starttls()
    server.login(sender_email, sender_password)
    server.sendmail(sender_email, recipient_email, msg.as_string())
