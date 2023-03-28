'''
Class, Object and Static Method
'''

class Student:

    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []

    def average(self):
        avg = sum(self.marks) / len(self.marks)
        print(avg)
        return avg

    @staticmethod
    def go_to_school():
        print("I'm going to school")

    def schooling(self):
        print("name of my school is: "+self.school)


avik = Student('Avik', 'UGHS')
shiv = Student('Shivam', 'NIT')

avik.marks.append(75)
avik.marks.append(80)

avik.average()
avik.go_to_school()
shiv.schooling()