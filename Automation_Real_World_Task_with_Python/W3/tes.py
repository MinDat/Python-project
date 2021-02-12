#!/usr/bin/env python3


import os
import json                         # Generate string to list - dict format
import sys
""" For generate PDF """
from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph, Spacer, Table, Image
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
""" ---------------- """


def data_table(filename):
    """Generate table format (list-list) form the given json file"""
    data = [["ID","Car", "Price", "Total Sales"]]                   # Header
    list_data = []                                                  # Storing list - dict

    with open(filename, "r") as json_file:
        text = json_file.read()
        """ ------------------------- """
        list_data = json.loads(text)                                # Generate text to list - dict format
        """ ------------------------- """

    for each_car in list_data:
        row = []                                                    # Temp row
        for key, value in each_car.items():                         # Access dict on json files
            if type(value) is dict:                                 # If the value have another dict
                a, b, c = value.values()                            # Take all value on that nest dict
                car = "{} {} ({})".format(a, b, c)
                row.append(car)
            else:
                row.append(value)
        data.append(row)                                            # Adding temp list into data table
    return data


def Generate_PDF(filename, title, table_data):
    """Generate PDF"""
    styles = getSampleStyleSheet()                                  # Set the default style for pdf
    report = SimpleDocTemplate("tes/report.pdf")                    # Link to the pdf director

    report_title = Paragraph(title, styles["h1"])
    empty_line = Spacer(1,20)                                                   # Adding Space between 2 line
    """-------------------------TABLE CONTENT------------------------------"""
    table_style = [('GRID', (0,0), (-1,-1), 1, colors.black),                   # Highlight grid of the table
                ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),                  # Bold the header
                ('ALIGN', (0,0), (-1,-1), 'CENTER')]                            # Aligning all text to center
    report_table = Table(data=table_data, style=table_style, hAlign="LEFT")
    """--------------------------------------------------------------------"""

    # Build PDF files by the given format list
    report.build([report_title, empty_line, report_table])


def main():
    # Look for the Json file
    for filename in os.listdir():
        if filename.endswith(".json"):
            break                                   # Exit loop and store json filename
        print("Not found Json file ...")
        exit(1)

    title = "Sales Summary for last month"      # Given title
    table_data = data_table(filename)               # Given data table format
    Generate_PDF(filename, title, table_data)       # Create PDF


main()


'''--------------------------------------------------------------------------------------------'''



'''--------------------------------------------------------------------------------------------'''



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
