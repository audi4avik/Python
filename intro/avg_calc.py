# Find average from a given list of numbers
num_list = [10, 20, 15, 22]

# print("avg: {}" .format(sum(num_list)/len(num_list)))

total = 0
for num in num_list:
    total = total + num
print(total/len(num_list))
