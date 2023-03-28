#Classes and Objects

class Car(object): #Class - blueprint for defining objects and methods

    def __init__(self, make, model): #initialize method ~ same as constructor

        self.brand = make #assigning attributes
        self.car = model

c1 = Car('Merc', 'SLS AMG') #c1 - instance of a class with values passed as reference
print(c1.brand)
print(c1.car)


