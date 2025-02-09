"""
Write an iterative function, gcdIter(a, b), that implements this idea. 

One easy way to do this is to begin with a test value equal to the smaller 
of the two input arguments, and iteratively reduce this test value by 1 
until you either reach a case where the test divides both a and b without 
remainder, or you reach 1.
"""
import sys



def gcdRecur(a, b):
    """
    g   = gcdRecur(a, b) 
        = gcdRecur(b, r0)
        = gcdRecur(r0, r1)
        = ... 
        = gcdRecur(rN−2, rN−1) = rN−1.
    """
    # the base case
    if b == 0:
        return a
    
    return gcdRecur(b, a % b)

    







tests = {
    (2,12): 2,
    (6, 12): 6,
    (9, 12): 3,
    (17, 12): 1
}


for args, expected in tests.items():
        s = gcdRecur(*args)
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