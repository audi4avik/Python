#Collection of strings. Tuples are like list but immutable.

cars = ["honda", "toyota", "nissan", "lexus", "ssanyong"]

length = len(cars)
print(length)

cars.append("mitsubishi")
print(cars)

cars.extend(['hyundai', 'yamaha'])
print(cars)

cars.insert(1, "suzuki")
print(cars)

print(cars.index("toyota"))

new_cars = cars.pop()
print(new_cars)
print(cars)

cars.remove("nissan")
print(cars)

print("*#" * 20)

slicing = cars[0:3]
slicing2 = cars[1:]
slicing3 = cars[:1]
slicing4 = cars[:-1]
slicing5 = cars[::2]
slicing6 = cars[::-1]
print(slicing)
print(slicing2)
print(slicing3)
print(slicing4)
print(slicing5)
print(slicing6)

print("**" *20)
print(cars)
cars.sort()
print(cars)

#Tuple

tuple = (1, 1, 2, 4, 3) #defining a tuple takes a parenthesis instead of a square brace like a list
print(tuple)
print(tuple[1]) #limited methods are available for tuple, although the methods are similar to list.
print(tuple[1:])
print(tuple.count(1))


# tuple[0] = 5 -- Item assignment is not possible like a list