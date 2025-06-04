
dictionaryField = {'Alice':30, 'Becky':30, 'Chris':30, 'Donald':30}

studentName = input("Enter Student's Name: ")

if studentName in dictionaryField:
    print(studentName + "'s marks: " + str(dictionaryField[studentName]))
else:
    print("Student Not Found")