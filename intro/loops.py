#for loop
people = ['john', 'Doe', 'pycharm', 454]    #this is a list

for element in people:
    print('current element: ', element)

#loop through sequence index
elements = ['Hi', 'Hello', 1.5, 'python']
for i in range(len(elements)):
    print('current element: ', elements[i])

#another for loop
for j in range(0,9):
    print(j)

print("*#" * 20)

#while loop
count = 0

while count <= 10:
    print('count', count)
    # count = count + 1  # pre increment
    if count==5:
        break
    count = count + 1 # post increment


