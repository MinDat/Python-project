#!/usr/bin/env python3

import re
import csv
import sys
import os

# Dictionary store the data
alert_count_per_user={}
messages_count={}

def create_data_dict():
    # Adding error when open files
    with open(sys.argv[1],'r') as log_file:
        for line in log_file:
            # search name of user
            pattern = r": +([A-Z]*) +(.*) \((.*)\)"
            result = re.search( pattern, line)
            # If the user have not exist in the list. setdefault for that user
            """------------------------------setdefault for a dict if that keys not in dict-----------------------------------"""
            if result[3] not in alert_count_per_user.keys():
                # Set the default of counting alert dict
                alert_count_per_user.setdefault(result[3], {"INFO":0,"ERROR":0})
            """---------------------------------------------------------------------------------------------------------------"""
            # Counting Infor and Error
            if "INFO" in line:
                alert_count_per_user[result[3]]["INFO"] += 1
            elif "ERROR" in line:
                alert_count_per_user[result[3]]["ERROR"] += 1

                # Count messages
                messages_count[result[2]] = messages_count.get(result[2], 0) + 1



def user_statistics():
    """Generate CSV that count how many times 1 user get ERROR and INFO messages"""
    #Creating csv format dict
    head = ["User name", "INFO", "ERROR"]
    row = []

    """---------------------------------------sorted in nest dict-------------------------------------------"""
    # sort by Username
    for name in sorted(alert_count_per_user.keys()):
        # add value to row format
        temp_dict = {}
        temp_dict["User name"] = name
        temp_dict["INFO"] = alert_count_per_user[name]["INFO"]
        temp_dict["ERROR"] = alert_count_per_user[name]["ERROR"]
        row.append(temp_dict)
    """-----------------------------------------------------------------------------------------------------"""

    #creating csv file
    with open("User_statistics.csv","w") as writer:
        writer = csv.DictWriter(writer, fieldnames = head)
        writer.writeheader()
        writer.writerows(row)


def error_messages():
    """Generate CSV that count how many times 1 message appear"""
    # sort the dict form the most common alert to rately alert
    sort_dict = {key: value for key, value in sorted(messages_count.items(), key = lambda x: x[1], reverse = True)}

    #Creating csv format dict
    head = ["Error name", "Count"]
    row = []

    # add value to row format
    for key, value in sort_dict.items():
        temp_dict = {}
        temp_dict["Error name"] = key
        temp_dict["Count"] = value
        row.append(temp_dict)

    #creating csv file
    with open("Error_messages.csv","w") as writer:
        writer = csv.DictWriter(writer, fieldnames = head)
        writer.writeheader()
        writer.writerows(row)


def main():

    # Adding command line argument
    if len(sys.argv) != 2:
        print("Please input the file the log file directory !!!")
        exit(1)
    """-----------------------------------------------------------------------------------------------------"""
    # Check csv extension of the file
    if ".csv" not in sys.argv[1]:
        print('Missing ".csv" file extension from first command-line argument!')
        print("Exiting program...")
        sys.exit(1)
    # check that csv file exists
    if not os.path.exists(sys.argv[1]):
        print("{} does not exist".format(sys.argv[1]))
        print("Exiting program...")
        exit(1)
    """-----------------------------------------------------------------------------------------------------"""


    create_data_dict()
    user_statistics()
    error_messages()
    exit(0)

main()
