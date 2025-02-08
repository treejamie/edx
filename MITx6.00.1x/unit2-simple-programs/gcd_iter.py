"""
Write an iterative function, gcdIter(a, b), that implements this idea. 

One easy way to do this is to begin with a test value equal to the smaller 
of the two input arguments, and iteratively reduce this test value by 1 
until you either reach a case where the test divides both a and b without 
remainder, or you reach 1.
"""
import sys



def gcdIter(a, b):
    # find the smaller value
    smaller = min(a, b)

    # now iterate and find the gcd
    for i in reversed(range(smaller)):

        # avoid DivisionByZeroErrors
        d = i + 1

        # if mod of a / d is zero, we have our number
        if all([ (a % d) == 0, b % d == 0 ]):
             return d






tests = {
    (2,12): 2,
    (6, 12): 6,
    (9, 12): 3,
    (17, 12): 1
}


for args, expected in tests.items():
        s = gcdIter(*args)
        # assert
        try:
            assert s == expected
            print("✅: success - {1} expected and {0} received".format(
                s,
                expected,
            ))
        except AssertionError:
            msg = "❌: error:\n\texpected: {1}\n\treceived: {0} ".format(
                s,
                expected,
            )
            sys.exit(msg)