animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')



def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    # biggesst is None
    biggest = {'key': None, 'len': 0}

    for k, v in aDict.items():
        if biggest['key'] is None or len(v)> biggest['len']:
            biggest['key'] = k
            biggest['len'] = len(v)

    return biggest['key']



print(biggest(animals))
