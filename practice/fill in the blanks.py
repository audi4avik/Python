"""
Create a To Do List. Continue to prompt for new item unless user enters a blank. Display the final To Do List.
"""
def get_blanks():
    """
    Docstring: this function is used for getting the words.
    """
    noun = input('Enter a Noun: ')
    verb = input('Enter a Verb: ')
    adj  = input('Enter an Adjective: ')
    return noun, verb, adj

def fill_blanks(blanks):
    """
        Docstring: this function is used for filling the blanks.
    """
    story = "In this course we will learn {0}. " \
            "It's always nice to {1} a language. " \
            "And it's so {2}!. ".format(blanks[0], blanks[1], blanks[2])
    return story

def display_story(story):
    """
        Docstring: this function is used for displaying the whole story.
    """
    print ()
    print ('** This is the story **')
    print (story)
    print ('')

def create_story():
    blanks = get_blanks()
    story = fill_blanks(blanks)
    display_story(story)


create_story()





