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



def car_name(dict):
    """ Create car name """
    a, b, c = dict["car"].values()                      # Take all value on that nest dict
    return "{} {} ({})".format(a,b,c)


def overal_sumary (json_format):
    """ Create report summary """
    #Find the most sales
    json_format.sort(key = lambda x: x["total_sales"], reverse = True)                                                  # Sort by sales in the list
    temp = json_format[0]                                                                                               # Take the highest sales in the list
    name = car_name(temp)
    most_sales = "The {} has the most sales: {}".format(name, temp["total_sales"])                                      # convert to string
    #Find the most revenue
    json_format.sort(key = lambda x: x["total_sales"]*float(x["price"][1:]), reverse = True)                            # Sort by total revenue in the list
    temp = json_format[0]                                                                                               # Take the highest revenue in the list
    name = car_name(temp)
    most_revenue = "The {} generated the most revenue: {}".format(name, temp["total_sales"]*float(temp["price"][1:]))   # convert to string

    # Create a temp dict (year: sum of sales)
    sales_per_year = {}
    for element in json_format:
        if element["car"]["car_year"] not in sales_per_year:
            sales_per_year[element["car"]["car_year"]] = element["total_sales"]
        else:
            sales_per_year[element["car"]["car_year"]] += element["total_sales"]
    #Find the most popular year
    a, b = sorted(sales_per_year.items(), key = lambda x: x[1], reverse = True)[0]                                      # Sort and take the highest sales in the dict
    most_popular_year = "The most popular year was {} with {} sales.".format(a, b)                                      # convert to string

    #Return a HTML string
    return most_revenue + "<br/>" + most_sales + "<br/>" + most_popular_year

def data_table(filename):
    """Generate table format (list-list) form the given json file"""
    data = [["ID","Car", "Price", "Total Sales"]]                       # Header
    json_format = []                                                    # Storing list - dict

    with open(filename, "r") as json_file:
        text = json_file.read()
        """ ------------------------- """
        json_format = json.loads(text)                                  # Generate text to list - dict format
        """ ------------------------- """

    for each_car in json_format:
        row = []                                                        # Temp row
        for key, value in each_car.items():                             # Access dict on json files
            if type(value) is dict:                                     # If the value have another dict
                a, b, c = value.values()                                # Take all value on that nest dict
                car = "{} {} ({})".format(a, b, c)
                row.append(car)
            else:
                row.append(value)
        data.append(row)                                                # Adding temp list into data table
    return data, json_format


def Generate_PDF(filename, title, info, table_data):
    """Generate PDF"""
    styles = getSampleStyleSheet()                                                  # Set the default style for pdf
    report = SimpleDocTemplate("Car_Sales_Report.pdf")                                    # Link to the pdf director

    report_title = Paragraph(title, styles["h1"])
    empty_line = Spacer(1,20)                                                       # Adding Space between 2 line
    report_info = Paragraph(info, styles["BodyText"])                               # Adding summary info
    """-------------------------TABLE CONTENT------------------------------"""
    table_style = [('GRID', (0,0), (-1,-1), 1, colors.black),                       # Highlight grid of the table
                ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),                      # Bold the header
                ('ALIGN', (0,0), (-1,-1), 'CENTER')]                                # Aligning all text to center
    report_table = Table(data=table_data, style=table_style, hAlign="LEFT")
    """--------------------------------------------------------------------"""

    # Build PDF files by the given FORMAT LIST
    report.build([report_title, empty_line, report_info, empty_line, report_table])


def main():
    # Look for the Json file
    for filename in os.listdir():
        if filename.endswith(".json"):
            break                                           # Exit loop and store json filename
        print("Not found Json file ...")
        exit(1)

    title = "Sales Summary for last month"                  # Given title
    table_data, json_format = data_table(filename)          # Given data table format
    info = overal_sumary(json_format)
    Generate_PDF(filename, title, info, table_data)         # Create PDF


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
