#using for loop
fact = 1
num = int(input('Enter any number to calculate the factorial: '))
for i in range(1, num+1):
    fact = fact * i
    print(fact)
print('the result is: ', fact)

#using while loop
# fact = 1
# num = int(input('Enter any number to calculate the factorial: '))
# i = 1
# while(i<=num):
#     fact = fact*i
#     i=i+1 #always specify the condition to stop the while loop from going into infinite
# print('the result is: ', fact)

