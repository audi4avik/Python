#functions

#create a function
def sayHi():
    print('Hi') #what will happen inside the function
sayHi() #calling the function

#Likewise
def printName(name):
    print('Hello', name)
#argument can be defaulted inside the function definition def printName(name = 'John'), although it can be overridden'
printName('Avik')   #passing an argument

#Return a value

def sum(num1,num2): #function defined with 2 variables
    total = num1+num2 #defined what to do with the variables or what happens inside the function.
    return total #what to be returned by the function

numSum = sum(4,7) #calling the function while passing the argument values to the function variables
print(numSum)
