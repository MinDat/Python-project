#!/usr/bin/env python3
"""++++++++++++++++++++++++++++JUST FOR REFERENCE++++++++++++++++++++++++++++"""
import email.message
import mimetypes
import os.path
import smtplib
import getpass

"""--------------Creates an email with an attachement.--------------------"""
# Basic Email formatting
email.message.EmailMessage()

sender = "me@example.com"
recipient = "you@example.com"
body = """Hey there!

    I'm learning to send emails using Python!"""

message['From'] = sender
message['To'] = recipient
message['Subject'] = 'Greetings from {} to {}!'.format(sender, recipient)
message.set_content(body)

# Process the attachment and add it to the email
attachment_path = "pdf/Car_Sales_Report.pdf"
attachment_filename = os.path.basename(attachment_path)
mime_type, _ = mimetypes.guess_type(attachment_path)
mime_type, mime_subtype = mime_type.split('/', 1)
with open(attachment_path, 'rb') as ap:
    message.add_attachment( ap.read(),
                            maintype=mime_type,
                            subtype=mime_subtype,
                            filename=os.path.basename(attachment_path))
"""-------------------------------------------------------------------------"""

"""--------------------Login--------------------"""
sender = "ruaninja16@gmail.com"
mail_pass = getpass.getpass('Password? ')
mail_server.login(sender, mail_pass)
"""---------------------------------------------"""

"""-----------Sends the message to the configured SMTP server.------------"""
mail_server = smtplib.SMTP('localhost')
mail_server.send_message(message)
mail_server.quit()
"""-------------------------------------------------------------------------"""
