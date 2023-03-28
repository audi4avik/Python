# Variables, Strings, Print, Methods
"""
Everything in Python is an Object. Every object has a type. Apple is an object of type String.
"""
print('Hello World')
#Data Types
a = 10 #int
b = 3.5 #float
name = 'My Name' #string
animals = ['dog', 'cat', 'tiger', 0] #list
color = ('red', 'green', 'blue') #tuple
car = {'Make': 'Ferrari', 'Mercedes': ['SLS AMG', 'SLK350', 'C63 AMG', 'Vision One']} #dict with mixed keys

'''
Python uses dynamic typing, meaning you can reassign variables to different data types. This makes Python very 
flexible in assigning data types; it differs from other languages that are statically typed.
'''

print (type (a))

a = a + a
print (a)

a = 'hello'
print(type (a))

income = 100000
tax_rate = 15
net_income = income - (income * tax_rate/100)
print (net_income)