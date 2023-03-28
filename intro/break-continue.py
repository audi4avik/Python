#break example
# while 1: #while 1: implies always true and while 0: implies always false
#     num = int(input("Enter a number (0 to quit): "))
#     if (num == 0):
#         break

#continue example
i = 1
while (i<=50):
    i = i+1
    if(i<=24):
        continue #loop inside the if will execute till 24, once it is 25 the if condition is false and it will come out.
    print(i)
