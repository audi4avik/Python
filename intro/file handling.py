#File handling

'''
w --> write only
r --> read only
r+ --> read $ write
a --> append
'''

#Writing to a file

myList = [1,2,3]

myFile = open("testFile.txt", "w")

for num in myList:
    myFile.write(str(num)+"\n")

myFile.close()

#Reading from a file

my_file = open("testFile.txt", "r")

print(str(my_file.read()))

my_file.close()

print("line by line")

my_file_line = open("testFile.txt", "r")
print(str(my_file_line.readline()))

my_file_line.close()


