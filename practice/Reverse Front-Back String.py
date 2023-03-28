'''
Given a string, return a new string where the
first and last chars have been exchanged.
'''

def front_back(string):

    if len(string) <= 1:
        return string

    else:
        mid = string[1:-1] #the ending is exclusive

        print(string[len(string) - 1] + mid + string[0])

        return string[len(string)-1] + mid + string[0]

front_back("m")
