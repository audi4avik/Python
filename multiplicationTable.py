# Multiplication table
number = int(input("Input a number: "))

# use for loop to iterate 10 times
for i in range(1, 11, 2):
    print(number, ' x ', i, ' = ', number * i)
