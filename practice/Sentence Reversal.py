'''
Reverse a sentence "this is it" = "it is this"
'''


def rev_sent():
    sentence = input("Enter the sentence to be reversed: ")
    '''
    split the string in elements of a list. 
    Pass argument to remove specific char while splitting the string
    '''
    result = sentence.split()

    # reverse the list!
    reversed_str = result[::-1]

    # join the list elements together. Blank indicates a space to be added
    sentence = " ".join(reversed_str)
    print(sentence)


rev_sent()
