'''
Given a non-empty string and an int n, return a new string where the char
at index n has been removed. The value of n will be a valid index of a char
in the original string (i.e. n will be in the range 0..len(str)-1 inclusive).
'''

def missing_char(str, n):
    if n in range(len(str)):
        print (str[n])
        str = str.replace(str[n], "")
        print(str)
        return str

    else:
        return str

missing_char("goat", 0)