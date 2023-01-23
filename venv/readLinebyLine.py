import csv
import json
from pathlib import Path

print("Please enter the name of a file to open for parsing:")
headerLine = []
headerListElements = []
dataLIST = []
dataListElements = []
fileVal = input("Enter file name here: ")
headercount = 0
datacount = 0

def createDictListFromCSVLists(dataElementList,headerElementList):
    finalDict = {}
    dictList = []
    for item in dataElementList:
        finalDict = dict(zip(headerElementList[0], item))
        dictList.append(finalDict)
    return(dictList)

with open(fileVal,"r") as csvFile:
    for line in csvFile:
        if "Data:" in line:
         headercount +=1
         print("Found Header before Data Dictionary:")
         print(headercount)
         datacount = 0
        else:
          if headercount==1:
             strippedLine = line.strip("\n")
             headerLine.append(strippedLine)
             headerListElements.append(strippedLine.split(","))
             print("Count equals ONE. Pull the header data out of this line.")
             print(headerListElements)
             headercount = 0
             datacount += 1
          else:
              strippedLine = line.strip("\n")
              if strippedLine.strip() == "":
                  datacount = 0
              if datacount > 0:
                  strippedLine = line.strip("\n")
                  dataLIST.append(strippedLine)
                  dataListElements.append(strippedLine.split(","))
                  print(dataListElements)
                  print(datacount)
                  datacount +=1


print("**************************************\n ")
print("Header Elements:")
print(headerListElements)
print("Data Elements:")
print(dataListElements)
print("**************************************\n ")

finalDataDictList = []

finalDataDictList = createDictListFromCSVLists(dataListElements,headerListElements)

print(finalDataDictList)
print("dictList length")
print(len(finalDataDictList))

print("Now to save JSON formatted data (List of dictionaries just created) to a json file.")
print("Your current working directory is: ")
print(Path.cwd())
finalDictval = input("Please enter a filename to be used to save the JSON output of the API:")

with open(finalDictval, "w") as outfile:
    json.dump(finalDataDictList, outfile)

with open(finalDictval,"r") as openfile:
    dataJsonList = json.load(openfile)

print("Data read back from file after saving new Data Dictionary List")

print(dataJsonList)

