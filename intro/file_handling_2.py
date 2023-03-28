#handling file without close() : with-as statement

print ("Start of write program")

with open("testFile.txt", "w") as fileWrite:
    fileWrite.write("This is a text written into the file")

print ("Start of read program")

with open("testFile.txt", "r") as fileRead:
    print(str(fileRead.read()))