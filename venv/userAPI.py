# Python program showing
# a use of input()

import requests

val = input("Enter your API URL value: ")
print(val)
print("Your api will be called:", val)
response = requests.get(val)
print(response.status_code)
print("Your API data shown in json format:")
print(response.json())