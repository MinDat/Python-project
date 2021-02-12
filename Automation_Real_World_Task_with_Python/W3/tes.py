#!/usr/bin/env python3

from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph, Spacer, Table, Image
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors




report = SimpleDocTemplate("tes/report.pdf")
styles = getSampleStyleSheet()
report_title = Paragraph("A Complete Inventory of My Fruit", styles["h1"])

table_style = [('GRID', (0,0), (-1,-1), 1, colors.black)]
table_data = [['elderberries', 1], ['figs', 1], ['apples', 2], ['durians', 3], ['bananas', 5], ['cherries', 8], ['grapes', 13]]
report_table = Table(data=table_data, style=table_style, hAlign="LEFT")

report.build([report_title, report_table])






# import smtplib, ssl
# import getpass
# from email.message import EmailMessage
#
#
# message = EmailMessage()
#
# sender = "me@example.com"
# recipient = "you@example.com"
#
# message['From'] = sender
# message['To'] = recipient
#
# message['Subject'] = 'Greetings from {} to {}!'.format(sender, recipient)
#
# body = """Hey there!
#
#     I'm learning to send emails using Python!"""
#
# message.set_content(body)
#
# port = 465  # For SSL
# password = getpass.getpass('Password? ')
#
# # Create a secure SSL context
# context = ssl.create_default_context()
#
# with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
#     server.login("my@gmail.com", password)
#     # TODO: Send email here
#     mail_server.send_message(message)
#     mail_server.quit()
