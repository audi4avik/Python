'''
programs for multiplication table
'''
# using for loop
num = int(input('Enter any number to see the multiplication table: '))
for i in range(1, 11):
    print(num,"*",i,"=",num*i)

# using while loop
num = int(input('Enter any number to see the multiplication table: '))
i =1
while (i <= 10):
    print(num, "*", i, "=", num * i)
    i = i + 1

"""
program for calculating exponential
"""
a = int((input("Enter the number: ")))
x = int(input("Enter the exponential: "))
result = 1
for i in range(1, (x+1)):
    result = result * a
    print(result) # what's happening inside the loop
print("Exponential of the given no is: ", result)



