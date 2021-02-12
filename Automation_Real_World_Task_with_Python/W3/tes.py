#!/usr/bin/env python3

from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph, Spacer, Table, Image
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors

import os
import glob
import json
import sys

def data_table(filename):
    data = [["ID","Car", "Price", "Total"]]
    list_data = []

    with open(filename, "r") as json_file:
        text = json_file.read()
        list_data = json.loads(text)

    for each_car in list_data:
        row = []
        for key, value in each_car.items():
            if type(value) is dict:
                a, b, c = value.values()
                car = "{} {} ({})".format(a, b, c)

                row.append(car)
            else:
                row.append(value)

        data.append(row)

    return data



def Generate_PDF(filename, title, table_data):
    styles = getSampleStyleSheet()
    report = SimpleDocTemplate("tes/report.pdf")

    report_title = Paragraph(title, styles["h1"])

    '''--------------------------------------------------------------------------------------------'''




    '''--------------------------------------------------------------------------------------------'''

    # table_data = [['elderberries', 1], ['figs', 1], ['apples', 2], ['durians', 3], ['bananas', 5], ['cherries', 8], ['grapes', 13]]


    table_style = [('GRID', (0,0), (-1,-1), 1, colors.black),                   # Highlight grid of the table
                ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),                  # Bold the header
                ('ALIGN', (0,0), (-1,-1), 'CENTER')]                            # Aligning all text to center

    report_table = Table(data=table_data, style=table_style, hAlign="LEFT")

    empty_line = Spacer(1,20)                                                   # Adding Space between 2 line
    # Build PDF files
    report.build([report_title, empty_line, report_table])

def main():

    for filename in os.listdir():
        if filename.endswith(".json"):
            break
        print("Not found Json file ...")
        exit(1)


    title = "A Complete Inventory of My Fruit"

    table_data = data_table(filename)
    print(table_data[1])

    Generate_PDF(filename, title, table_data)



main()




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
