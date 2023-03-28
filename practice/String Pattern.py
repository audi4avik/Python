'''
Given a non-empty string like "Code" return a string like "CCoCodCode".
'''

def string_splosion(str):

    result=""
    for i in range(len(str)):
        result = result+str[:i+1]
    print(result)
    return result

string_splosion("cow")