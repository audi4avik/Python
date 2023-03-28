'''
Create a class. Define 3 methods inside it.
Create a child class. Inherit the properties from the parent class.
Override some of the properties in child class. Overrride a single method completely and also override a method
with extra functionality while keeping the base functionality.
'''


class Computer(object):     # Parent class

    def __init__(self):
        print("\nThis is a computer")

    def display(self):
        print("It has a display")

    def keyboard(self):
        print("It has a keyboard")

    def processor(self):
        print("It runs on i5 processor")


class Laptop(Computer):     # Passing the parent class to be inherited in child.

    def __init__(self):     # Initializing child class
        Computer.__init__(self)     # Initializing the parent class inside child, code runs without this also.
        print("This is a Laptop instance of Computer class")

    def keyboard(self):     # Overriding parent class with child class properties
        print("the keyboard is attached with laptop")

    def display(self):  # Overriding with child class property while keeping the parent class property.
        super(Laptop, self).display()
        print("The display size is 11 inch")

    def webcam(self):   # Unique feature of child class.
        print("This laptop has a webcam attached")



c = Computer()
c.display()
c.processor()
c.keyboard()


l = Laptop()
l.processor()   # Directly inherited from parent
l.keyboard()    # Overriding the parent
l.display()     # Overriding the parent  with new property while keeping the parent property
l.webcam()      # Unique property of child


