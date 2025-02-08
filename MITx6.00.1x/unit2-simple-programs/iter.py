import sys


def iterPower(base, exp):

    # edge cases
    if exp == 0:
        return 1.0000
    elif exp == 1:
        return base
    
    # stash the result
    result = 0

    # now do the thing
    while exp > 1:
        if result == 0:
            result = base * base
        else:
            result = result * base

        exp -= 1

    return round(result, 4)



tests = {
    (6, 6): 46656,
    (9.47, 10): 5800958920.6513,
    (-0.02, 0): 1.00,
    (0.37, 1): 0.3700
}


for args, expected in tests.items():
        s = iterPower(*args)
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



sys.exit()




def recurPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    # Your code here
    if exp == 1:
        return base
    elif exp < 1:
        return 1
    
    return base * recurPower(base, exp -1)


foo = recurPower(5, 5)