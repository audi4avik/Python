# 3 - Fizz 5 - Buzz 3x5 - FizzBuzz

def fizzbuzz():

    # testcases = int(input("Enter no of test case: "))
    # while
    #     num = int(input("Enter no of test case: "))

    num = 1
    while num <= 100:
        if num%3 == 0 and num%5 == 0:
            print("FizzBuzz")
        elif num%3 == 0:
            print("Fizz")
        elif num%5 == 0:
            print("Buzz")
        else:
            print(num)
        num += 1

fizzbuzz()