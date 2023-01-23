import json
from pathlib import Path

print("Please enter the name of a file to open for parsing:")
print("Current directory PATH name :")
print(Path.cwd())

headerLine = []
headerListElements = []
dataLIST = []
dataListElements = []

def createDictListFromCSVLists(dataElementList,headerElementList):
    finalDict = {}
    dictList = []
    for item in dataElementList:
        finalDict = dict(zip(headerElementList[0], item))
        dictList.append(finalDict)
    return(dictList)

fileVal = input("Enter file name here: ")
fileObj = Path.cwd() / fileVal

headercount = 0

with open(fileObj,"r") as csvFile:
    for line in csvFile:
        if headercount ==0:#Headers are on first line of CSV FILE - strip the newline character
            strippedLine = line.strip("\n")
            headerLine.append(strippedLine)
            headerListElements.append(strippedLine.split(","))#Now take the header fields save them ina Python LIST[]
            print("Count equals ZERO. Pull the header data out of this line.")
            print(headerListElements)
            headercount+=1#bump the headercount to ONE to indicate that we got the headers
        else:#headers have been found - grab data elements
            strippedLine = line.strip("\n")
            dataLIST.append(strippedLine)
            dataListElements.append(strippedLine.split(","))
            print(dataListElements)

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