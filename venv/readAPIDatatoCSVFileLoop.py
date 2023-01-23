# Python program showing
# a use of input()
import time

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

print("Now to save JSON formatted data to a json file.")
print("Your current working directory is: ")
print(Path.cwd())
fileval = input("Please enter a filename to be used to save the JSON output of the API (read from a file):")

fileObj = Path.cwd() / fileval

print(fileObj)

def readAPIDataSavetoFile(urlObj, fileval):
    response = requests.get(urlObj)
    print(response.status_code)
    print("Your API data shown in json format:")
    print(response.json())
    print("Attempting to open the file: ")
    print(fileval)
    print("Checking if file exists: ")
    if (fileval.exists()):
        print("File value exists: " + fileval.as_posix())
        with open(fileval, "a") as outfile:
            json.dump(response.json(), outfile)
    else:
        print("File does not exist - open it for writing")
        with open(fileval, "w") as outfile:
            json.dump(response.json(), outfile)

    json_object = response.json()

    return json_object


def getSelectiveDictionary(dict, itemStr):
    newDict = {}

    for key in dict.keys():
        if key != itemStr:
            value = dict[key]
            newDict[key] = value

    return newDict


def writeCSVFile(jsonDict, jsonFileObj, csvFileObj, urlObj):
    outerdatadictionary = jsonDict
    innerdatadictionary = jsonDict['Data']
    datadictlist = jsonDict['Data']['Data']
    newinnerdatadict = getSelectiveDictionary(innerdatadictionary,"Data")
    newouterdatadict = getSelectiveDictionary(outerdatadictionary,"Data")
    testDict = {}
    print("\n***********")
    print("Outer Dictionary:")
    print(outerdatadictionary)
    print("\n***********")
    print("Inner Dictionary")
    print(innerdatadictionary)
    print("\n***********")
    print("Data Dictionary List")
    print(datadictlist)
    print("\n**************************")
    print("Checking existence of the csv file:")
    print("URLObj:")
    print(urlObj)
    print("CsvFile: ")
    print(csvFileObj.as_posix())
    print("fileObj(JSON):")
    print(fileObj.as_posix())
    innerDictLabel = ["Data Attributes:"]
    dataDictLabel = ["Data: "]
    if (csvFileObj.exists()):
        print("CSVFILE EXISTS - append data to file")
        with open(csvFileObj, "a") as newoutfile:
            csv_writer = csv.writer(newoutfile)

            csv_writer.writerow("")
            csv_writer.writerow(newouterdatadict.keys())
            csv_writer.writerow(newouterdatadict.values())
            csv_writer.writerow("")
            csv_writer.writerow(innerDictLabel)
            csv_writer.writerow(newinnerdatadict.keys())
            csv_writer.writerow(newinnerdatadict.values())
            csv_writer.writerow("")
            csv_writer.writerow(dataDictLabel)
            count = 0
            for sample in datadictlist:
                if count == 0:
                    header = sample.keys()
                    csv_writer.writerow(header)
                    count += 1
                csv_writer.writerow(sample.values())

    else:
        print("CSV FILE DOES NOT Exist - start / create a new file.")
        outHeaderFileInfo = []
        now = datetime.now()
        print("now =", now)
        date_time_string = now.strftime("%m/%d/%Y %H:%M:%S")
        outHeaderFileInfo.append("Data file: " + jsonFileObj.as_posix())
        outHeaderFileInfo.append(date_time_string)
        outHeaderFileInfo.append("CSV file:  " + csvObj.as_posix())
        outHeaderFileInfo.append("Generating URL: " + urlObj)

        with open(csvFileObj,"w") as newfile:
            csv_writer = csv.writer(newfile)

            csv_writer.writerow(outHeaderFileInfo)

            csv_writer.writerow("")
            csv_writer.writerow(newouterdatadict.keys())
            csv_writer.writerow(newouterdatadict.values())
            csv_writer.writerow("")
            csv_writer.writerow(innerDictLabel)
            csv_writer.writerow(newinnerdatadict.keys())
            csv_writer.writerow(newinnerdatadict.values())
            csv_writer.writerow("")
            csv_writer.writerow(dataDictLabel)

            count = 0
            for sample in datadictlist:
                if count == 0:
                    header = sample.keys()
                    csv_writer.writerow(header)
                    count += 1
                csv_writer.writerow(sample.values())

    return (jsonDict)


jsonDict = {}
innerDictionary = {}
outerDictionary = {}
newinnerDictionary = {}
newOuterDictionary = {}
dataDictList = {}
outHeaderFileInfo = []

jsonDict = readAPIDataSavetoFile(urlObj, fileObj)


# datetime object containing current date and time

csvval = input("Please enter a filename {.csv} to be used to save the JSON output of the API (as a CSV file):")

csvObj = Path.cwd() / csvval

testDict = {}

print(testDict)

while True:
    localtime = time.localtime()
    result = time.strftime("%I:%M:%S %p", localtime)
    print(result)
    testDict = writeCSVFile(jsonDict, fileObj, csvObj, urlObj)
    time.sleep(10)
