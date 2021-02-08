#!/usr/bin/env python3

import sys
import os

def fname():
    pass

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

    print(title)
    exit(0)

main()
