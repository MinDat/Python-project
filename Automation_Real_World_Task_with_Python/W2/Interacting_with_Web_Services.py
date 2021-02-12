#!/usr/bin/env python3

import os
import requests

feedback = []
def main():
    lists = os.listdir("feedback")
    # print(lists)
    for file in lists:
        if file.endswith(".txt"):

            customer_feedback = {}
            # print("d")
            with open("feedback/"+file, "r") as text:
                lines = list(text)
                customer_feedback["Title"] = lines[0][:-1]
                customer_feedback["Name"] = lines[1][:-1]
                customer_feedback["Time"] = lines[2][:-1]
                customer_feedback["Comment"] = lines[3][:-1]

            response = requests.post("http://35.225.95.53/feedback/",json = customer_feedback)
            print('Response',response.status_code)
            feedback.append(customer_feedback)

    # for data in feedback:
    #     print(data)
    #     print()

main()
