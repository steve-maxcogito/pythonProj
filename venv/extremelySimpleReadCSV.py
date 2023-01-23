import pandas as pd
from pathlib import Path
import json

print("Please enter the name of a file to open for parsing:")
print("Current directory PATH name :")
print(Path.cwd())

# displaying the contents of the CSV file
fileVal = input("Enter file name here: ")
fileObj = Path.cwd() / fileVal

headercount = 0

with open(fileObj,"r") as csvFile:
    csvFile = pd.read_csv(fileObj,"r")# reading the CSV file

# displaying the contents of the CSV file

print(csvFile.to_string())
print("*****************************************\n")
print("As dictionary-****************************")

newDictionary = {}

newDictionary = csvFile.to_dict()

print(newDictionary)

print("Please enter the name of a file to open for writing these data as JSON:")
print("Current directory PATH name :")
print(Path.cwd())

# displaying the contents of the CSV file
fileVal = input("Enter file name here: ")
fileObjJson = Path.cwd() / fileVal

with open(fileObjJson,"w") as jsonfile:
    json.dump(newDictionary,jsonfile)