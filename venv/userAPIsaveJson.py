# Python program showing
# a use of input()

import requests
import json
from pathlib import Path
import pandas as pd

val = input("Enter your API URL value: ")
print(val)
print("Your api will be called:", val)
response = requests.get(val)
print(response.status_code)
print("Your API data shown in json format:")
print(response.json())

print("Now we will read out the JSON data from the file where it was saved.")

print("***********************************")
print("READING Data from file:")
print("***********************************")
# Opening JSON file for READING
with open(val, 'r') as openfile:
    # Reading from json file
    json_object = json.load(openfile)

# Printing the result

print("***********************************")
print("Data READ from file:")
print("***********************************")

print(json_object)

print("***********************************")
print("END OF READING Data from file:")
print("***********************************")