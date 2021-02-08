#!/usr/bin/env python3

import sys
import os
import csv


def read_csv(csv_file):
    """ Read data form CSV files """
    with open(csv_file, "r") as files:
        data = csv.reader(files)
        return list(data)

def html_content(data, title):
    """ Read the content form CSV and generate html text file"""
    # add html header into text
    html_text = """
    <!DOCTYPE html>
    <html>
    <head>
    <style>
    table {
      width: 25%;
      font-family: arial, sans-serif;
      border-collapse: collapse;
    }

    tr:nth-child(odd) {
      background-color: #dddddd;
    }

    td, th {
      border: 1px solid #dddddd;
      text-align: left;
      padding: 8px;
    }
    </style>
    </head>
    """

    # Starting body of html
    html_text += "<body>"

    # adding title
    html_text += "<h2> {} </h2>".format(title)

    # Adding table content
    html_text += "<table>"
    # Each row in table
    for index, row in enumerate(data):
        #Each collumn in table
        html_text += "<tr>"
        if index == 0:
            # Table Head
            for name in row:
                html_text += "<th>{}</th>".format(name)
        else:
            # Table body
            for element in row:
                html_text += "<td>{}</td>".format(element)
        # Exit collumn
        html_text += "</tr>"
    # Exit row
    html_text += "</table>"
    # End of html
    html_text += """</body>
                    </html>"""
    # Return
    return html_text


def create_html(content, html_dir):
    """create html files"""
    with open(html_dir, "w") as f:
        f.write(content)


def main():
    #adding command line arguments
    if len(sys.argv) < 3:
        print("Please input by the format: \"./python_name.py <csv directory> <html directory>\" !")
        exit(1)

    #create var store directory
    csv_file = sys.argv[1]
    html_file = sys.argv[2]

    # check if these file is not contain extension
    if ".csv" not in sys.argv[1]:
        print("Your file {} does not contain \".csv\"".format(sys.argv[1]))
        exit(1)

    # check if these file directory exists
    if not os.path.exists(sys.argv[1]):
        print("Your csv does not exists in the directory !")
        exit(1)

    # take the file_name csv as an title
    title = os.path.splitext(os.path.basename(csv_file))[0].replace("_"," ").title()

    # call sub function
    data = read_csv(csv_file)
    content = html_content(data, title)
    create_html(content, html_file)
    exit(0)

if __name__ == "__main__":
    main()
