'''
Implement fibonacci numbers
'''


def gen_fib():
    count = int(input("How many fibonacci numbers would you like to generate? "))
    i = 1
    if count == 0:
        fib = []
    elif count == 1:  # fib 1 = 0
        fib = [0]
    elif count == 2:  # fib 2 = 0, 0+1,
        fib = [0, 1]
    elif count > 2:  # fib 4 = 0,1,1,2
        fib = [0, 1]  # initialize the list
        while i < (count - 1):  # i.e. count = 5; i = 1 > True
            fib.append(fib[i] + fib[i - 1])  # append the sum of previous 2 to the existing list fib[1]+ fib[0]
            i += 1  # increment i for the next element

    print(fib)
    return fib


gen_fib()
