'''
Given a string and a non-negative int n,
return a larger string that is n copies of the original string.
'''

def string_times(str, n):

    if n > 0:
        for i in range(n):
            print(str*n)
            return str*n
    else:
        print(str)
        return str

string_times("abcv", 5)