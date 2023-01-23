# Python program showing
# a use of input()

import requests
import json
import pandas as pd
import csv
from datetime import datetime
from pathlib import Path

val = input("Enter your API URL value: ")
print(val)
print("Your api will be called:", val)
urlObj = val
response = requests.get(val)
print(response.status_code)
print("Your API data shown in json format:")
print(response.json())

#now we convert json data to CSV (comma separated value) file
outerDictionary = {}
innerDictionary = {}
dataDictList = []
outHeaderFileInfo = []
outerHeaderList = []
innerHeaderList = []
dictionaryDataHeaderList = []

print("Please enter the name of a data file that will contain the data that we just printed")

print("Now to save JSON formatted data to a json file.")
print("Your current working directory is: ")
print(Path.cwd())
val = input("Please enter a filename to be used to save the JSON output of the API (read from a file):")

with open(val, "w") as outfile:
    json.dump(response.json(), outfile)

    # Opening JSON file
with open(val, 'r') as openfile:
    # Reading from json file
    json_object = json.load(openfile)

print("***********************************")
print("READING Data from file:")
print("***********************************")

print(json_object)

#start building the file header and relevant headers for the CSV file

# datetime object containing current date and time

csvval = input("Please enter a filename {.csv} to be used to save the JSON output of the API (as a CSV file):")

now = datetime.now()
print("now =", now)
dt_string = now.strftime("%m/%d/%Y %H:%M:%S")
outHeaderFileInfo.append("Data file: "+val)
outHeaderFileInfo.append(dt_string)
outHeaderFileInfo.append("CSV file:  "+csvval)
outHeaderFileInfo.append("Generating URL: "+urlObj)

print(outHeaderFileInfo)

#grab outer data for headers; remember that outer Headers are in the main dictionary of the response

outerDictionary = response.json()

print(outerDictionary.keys())

innerDictionary = outerDictionary['Data']
dataDictList = outerDictionary['Data']['Data']

print("\n")
print(innerDictionary.keys())

def getList(dict):
      list = []
      for key in dict.keys():
          list.append(key)

      return(list)

def getSelectiveList(list,itemVal):
    newList = []
    for p in list:
        if p != itemVal:
            newList.append(p)

    return newList

def getSelectiveDictionary(dict,itemStr):
    newDict = {}

    for key in dict.keys():
        if key!=itemStr:
            value = dict[key]
            newDict[key] = value

    return newDict


innerHeaderList = getList(innerDictionary)
print("INNER HEADER LIST before FILTERING : ")
print(innerHeaderList)
print("\n")
print("INNER HEADER LIST AFTER FILTERING" )
innerHeaderList = getSelectiveList(innerHeaderList,"Data")
print(innerHeaderList)

newinnerDictionary = {}
newOuterDictionary = {}

newinnerDictionary = getSelectiveDictionary(innerDictionary,"Data")
newOuterDictionary = getSelectiveDictionary(outerDictionary,"Data")
print("Unfiltered inner dictionary keys: ")
print(innerDictionary.keys())
print("Unfiltered inner dictionary values: ")
print(innerDictionary.values())

print("Unfiltered outer dictionary keys: ")
print(outerDictionary.keys())
print("Unfiltered outer dictionary values: ")
print(outerDictionary.values())

print("Selective dictionary keys:")
print(newinnerDictionary.keys())
print("Selective dictionary values:")
print(newinnerDictionary.values())

datafile =open(csvval,"w")

csv_writer = csv.writer(datafile)

csv_writer.writerow(outHeaderFileInfo)
csv_writer.writerow("")
csv_writer.writerow(newOuterDictionary.keys())
csv_writer.writerow(newOuterDictionary.values())
csv_writer.writerow("")
csv_writer.writerow(newinnerDictionary.keys())
csv_writer.writerow(newinnerDictionary.values())
csv_writer.writerow("")

count = 0

for sample in dataDictList:
    if count == 0:
      header = sample.keys()
      csv_writer.writerow(header)
      count += 1

    csv_writer.writerow(sample.values())

datafile.close()