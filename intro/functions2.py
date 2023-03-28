#functions w/o arguments

def add():
    n1 = int(input("Enter a number: "))
    n2 = int(input("Enter another number: "))
    print(n1+n2)

add()

#functions with return statement

def multiply():

     n1 = int(input("Enter a number: "))
     n2 = int(input("Enter another number: "))
     return n1 * n2

result = multiply()
print("the result is: ",result)

#functions with arguments

def isGerman():
    inputCars = input('Enter the brand of the car: ')
    listCars = ['Audi', 'BMW', 'Ferrai', 'Merc']
    if inputCars in listCars:
        return print('Selected car is German')
    elif inputCars == 'Ferrari':
        return print('car is not German')
    else:
        print ('car is not listed')

isGerman()



