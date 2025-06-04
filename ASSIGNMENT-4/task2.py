try:
    fileName = 'output.txt'
    appendFile = open(fileName, 'a')

    firstLine = input("Enter text to write to the file: ")
    appendFile.write(firstLine + "\n")
    print("Data Successfully written to ", fileName)

    secondLine = input("Enter additional text to append to the file: ")
    appendFile.write(secondLine + "\n")
    print("Data Successfully appended to ", fileName)
    appendFile.close()

    print("Final Content of", fileName, ":")

    readFile = open(fileName, 'r')
    fileContent = readFile.read()
    print(fileContent)
    readFile.close()
except FileNotFoundError:
    print("The File '" + str(fileName) + "' was not found")