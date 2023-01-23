#Python script to download files
import requests

fileNameUrl = input("Please input URL where the file exists:")
fileName = input("Please input a LOCAL file name for teh file we will download (file on this system):")

def download(url, file_name):
    # open in binary mode
    with open(file_name, "wb") as file:
        # get request
        response = requests.get(url)
        # write to file
        file.write(response.content)
        return(response.status_code)


print("Calling download method with:")
print(fileNameUrl)
print("Local file name:")
print(fileName)

statusCode =download(fileNameUrl,fileName)

print(statusCode)