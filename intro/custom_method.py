'''
Class and object contd.
'''

class Car(object):

    wheelSize = 19 # member variable - available across the whole class

    def __init__(self, make, model):
        self.brand = make # instance variable - these are changing with the instances declared outside
        self.type = model

    def carInfo(self): # custom method

        print("make of the car: " + self.brand)
        print("model of the car: " + self.type)

print(Car.wheelSize) # accessing member variable anywhere inside the class

c1 = Car('BMW', 'M8 GTE') #brand and type objects are passed here while creating the instance
c1.carInfo()
print(c1.wheelSize)

c2 = Car('Audi', 'R8 LMS')
c2.carInfo()
c2.wheelSize = 20  # incorrect place to define, mixing up member variable with instance variable
print(c2.wheelSize)