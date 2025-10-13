fileOne = input("Enter the name of the first file: ")
fileTwo = input("Enter the name of the second file: ")

with open(fileOne, 'r') as fileOne, open(fileTwo, 'w') as fileTwo:
    content = fileOne.read()

    fileTwo.write(content)
