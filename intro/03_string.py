# String handling and methods in python
# len() lower() upper() str() replace()

myStr = "AvikD"
num = 10

print(myStr[4])
print(len(myStr))
print(myStr.lower())
print(myStr.upper())
print(str(num) + " = Diego")
print(myStr.replace('v','bh'))

print("\n")
print ("*#"* 30)
print("\n")

newStr = "This is a sentence"
print(newStr[:])
print(newStr[2:])
print(newStr[0:14:2])
print(newStr[:-2]) #from last it counts as negative towards start
print(newStr[:len(newStr)-2]) #same as above
print(newStr[::-1]) #reversal of string by making the steps negative
print(newStr[0:4]) #Although the string was reversed above, due to the immutable property the change was not permanent


str1 = "NYC"
str2 = "LA"
print("Welcome to %s and enjoy your gambling in %s." %(str1, str2))
