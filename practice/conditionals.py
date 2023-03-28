#Conditionals

output = 10 == int(20/1.99) #Type casting in python
print(output)

a=7
if a < 5:
    print('this is true') #anything in the same indent holds inside the loop


#print('this is outside of the if statement') #out of indent

#if else
if a < 6:
    print('this is also true')
else:
    print('this is false')

#elif
color='yellow'

if color=='yellow':
    print('color is red')
elif color=='blue':
    print('color is blue')
else:
    print('color is neither red or blue')

#nested if
if color=='yellow':
    if a < 10:
        print('color is yellow and a is not 10')

#use of logical operator
if color=='yellow' and a < 8:
    print('color is yellow and a is not 8')