
try:
    fileName = 'sample.txt'
    readFile = open(fileName, 'r')
    fileContent = readFile.read()
    print(fileContent)
    readFile.close()
except FileNotFoundError:
    print("The File '" + str(fileName) + "' was not found")