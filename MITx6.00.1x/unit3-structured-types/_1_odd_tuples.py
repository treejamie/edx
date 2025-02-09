"""
Write a procedure called oddTuples, which takes a tuple as input, and returns
a new tuple as output, where every other element of the input tuple is copied,
starting with the first one. So if test is the tuple ('I', 'am', 'a', 'test', 'tuple'),
then evaluating oddTuples on this input would return the tuple ('I', 'a', 'tuple')
"""


def oddTuples(aTup):
    foo = ()
    for i, t in enumerate(aTup):
        if i % 2 == 0:
            foo += t,

    return foo


x = ('I', 'am', 'a', 'test', 'tuple')

assert oddTuples(x) == ('I', 'a', 'tuple')