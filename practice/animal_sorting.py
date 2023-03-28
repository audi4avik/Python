unsorted_file = 'animals.txt'
sorted_file = 'animals-sorted.txt'

try:
    with open(unsorted_file) as animals:
        animal_list = []
        for animal in animals:
            animal_list.append(animal)
        animal_list.sort()

except:
    print("Could not open {}.".format(unsorted_file))

try:
    with open(sorted_file, 'w') as animals_sorted:
        for animal in animal_list:
            animals_sorted.write(animal)

except:
    print("Could not open {} for writing.".format(sorted_file))
