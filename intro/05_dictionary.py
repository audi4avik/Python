#dictionary is mutable - change values runtime. Works as a key value pair.

car = {'bmw': {'model': '550d', 'hp': '430PS', 'year': 2016}, 'merc': {'model': 'SLS AMG', 'hp': '570PS', 'year': 2015}, 'audi': {'model': 'R8 V10', 'hp': '520PS', 'year': 2018}}

print(car['bmw'])
print(car['merc']['model'])
print(car['audi']['hp'])

print(car.keys())
print(car.values())
print(car.items())

print('**'*100)
car_copy = car.copy()
print(car_copy)

print('#*'*100)
print(car_copy.pop('bmw'))
print(car_copy)

print('*#'*100)
print(car_copy.clear())



