# Python program to read
# json file


import json

# Opening JSON file
from pathlib import Path

f = open('data.json',"r")

# returns JSON object as
# a dictionary
data = json.load(f)
# Declare a python LIST

dataList = []

#Declare a python dictionary

dataDict = {}

#The entire set of data is a LIST of various things
#The entire "outer" List is called DATA and there is an internal list ALSO called data
#Set the dataList to point to the internal LIST called Data

dataList = data['Data']['Data']

print("********************  Printing a list of the data items that are dictionaries of key/value pairs ***********")

print(dataList)

dataJsonList = []

print("Please enter the name of a data file that will contain the data that we just printed")

print("Now to save JSON formatted data to a json file.")
print("Your current working directory is: ")
print(Path.cwd())
val = input("Please enter a filename to be used to save the JSON output of the API (read from a file):")

with open(val, "w") as outfile:
    json.dump(dataList, outfile)

with open(val,"r") as openfile:
    dataJsonList = json.load(openfile)

print("*******************************")
print("********************  Printing a list of the data items that are read from the JSON file : ***********")
print("*******************************")

print(dataJsonList)


dataDict = dataList[0]

print("********************  Printing the first of the data items that are dictionaries of key/value pairs ***********")

print(dataDict)

newDataList = []

list_len = len(newDataList)

print("Length of the newDataList (before adding any items to the LIST:", list_len)

print("******************** Now we are adding the items read from the LIST of data dictionaries to a new LIST in a for LOOP ***********")
print("******************** This illustrates how to access just the price data dictionaries and add them to a LIST for further processing ***********")

for i in dataList:
    newDataList.append(i)

list_len = len(newDataList)

print("Length of the newDataList:", list_len)
print("******************************************************")
print("Now we will print out the new data LIST we just built.")
print("******************************************************")
print("New Data List itself: ")

print(newDataList)

print("Now we will save these new data to a new ouptut File.")

print("Now to save JSON formatted data to a json file.")
print("Your current working directory is: ")
print(Path.cwd())
val = input("Please enter a filename to be used to save the JSON output of the API:")

#jsonDictOutput = json.load(newDataList)

with open(val, "w") as outfile:
    json.dump(newDataList, outfile)

with open(val,"r") as openfile:
    dataJsonList = json.load(openfile)

print("Data read back from file after saving new Data Dictionary List")

print(dataJsonList)


