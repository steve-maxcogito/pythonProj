import csv
import json
#from datetime import datetime
from pathlib import Path

filenameVal = input("Please input a file that contains JSON:")

outerDict = {}
dataDictList = []

with open(filenameVal,"r") as file:
    outerDict = json.load(file)

print("File data from file: ")
print(outerDict)

dataDictList = outerDict['Data']['Data']


print("List of data dictionaries: ")
print(dataDictList)

csvFile = input("Please enter a file name for the CSV file: ")
print("User entered:")
print(csvFile)
headers = dataDictList[0].keys()

with open(csvFile,"w") as csvfile:
    writer = csv.DictWriter(csvfile,headers)
    writer.writeheader()
    writer.writerows(dataDictList)

print("\nDone writing CSV file")

