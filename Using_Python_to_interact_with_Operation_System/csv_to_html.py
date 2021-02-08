#!/usr/bin/env python3

import sys
import os
import csv



def read_csv_create_text_file(csv_file, title):
    """ Read the content form CSV and generate html text file"""
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
    <body>
    """

    html_table = "<table><tr>"

    with open(csv_file, "r") as files:
        f = csv.reader(files)
        for index, row in enumerate(f):

            table_block = ""

            if index == 0:
                for name in row:
                    table_block += "<th>{}</th>".format(name)
            else:
                for element in row:
                    table_block += "<td>{}</td>".format(element)

            html_table += table_block + "</tr><tr>"

        html_table += "</tr></table>"

    html_text += (html_table + "</body></html>")
    print(html_text)
    with open("test.html", "w") as f:
        f.write(html_text)


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



    read_csv_create_text_file(csv_file, title)
    exit(0)

if __name__ == "__main__":
    main()
