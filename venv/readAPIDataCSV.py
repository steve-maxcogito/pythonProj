import csv


myFile = open('steveDataAPIsave2.csv',"r")
print("The content of CSV file is:")
text_list = myFile.readlines()
dataLIST = []
headerList = []
dataLISTElements = []
headerListElements = []
count = 0
for line in text_list:
    if "Data:" in line:
        print("Found Header before Data Dictionary:")
        if count == 0:
            count +=1
    else:
        if count >=1:
            if count ==1:
                if '\n' in line:
                    print("Header Line ends with newLine")
                    strippedLine = line.strip("\n")
                    headerList.append(strippedLine)
                    headerListElements.append(strippedLine.split(","))
                else:
                    headerList.append(line)
                    headerListElements.append(line.split(","))
                count +=1
            else:
                if '\n' in line:
                    print("Data Line ends with newLine")
                    strippedDataline = line.strip("\n")
                    dataLIST.append(strippedDataline)
                    dataLISTElements.append(strippedDataline.split(","))
                else:
                    dataLIST.append(line)

            print(line)

print(headerList)
print(len(headerList))
print(dataLIST)
print(len(dataLIST))

print("Header List elements:")
print(headerListElements)
print(len(headerListElements))
print("Data LIST elements:")
print(dataLISTElements)
print(len(dataLISTElements))

dictList = []
FinalheaderList = headerListElements[0]
FinaldataList = dataLISTElements[0]
print("Final Header List:")
print(FinalheaderList)
TeempdataDict = {}
TempdataDict = dict(zip(FinalheaderList,FinaldataList))
print(TempdataDict)

for item in dataLISTElements:
    TempdataDict = dict(zip(FinalheaderList, item))
    dictList.append(TempdataDict)

print("After building List of dictionary elements:")

print(dictList)

myFile.close()