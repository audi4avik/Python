def display_facts(facts):
    for fact in facts:
        print('{}: {}'.format(fact, facts[fact]))
    print()


facts = {
    'Jeff':  'afraid of dogs',
    'David': 'Plays guitar',
    'Jane':  'likes to dance'
}

# printing original dictionary
display_facts(facts)

# mutable, changing properties runtime
facts['Jeff'] = 'is afraid of heights'
facts['John'] = 'playing real racing'
display_facts(facts)





