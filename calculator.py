# Take input of 2 numbers and calculate based on choice
number1 = int(input("Enter value of first number: "))
number2 = int(input("Enter value of second number: "))
operator = input("Choose one operator from this list / * + - : ")
result = ""

if operator == '/':
    result = number1 / number2
elif operator == '*':
    result = number1 * number2
elif operator == '+':
    result = number1 + number2
elif operator == '-':
    result = number1 - number2
else:
    print("invalid operator, please retry!")

print("Calculated value: " + str(result))
