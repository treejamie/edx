import sys


def isIn(char, aStr):
    # base case = empty string
    if aStr == '':
         return False

    if char == aStr[0] or char == aStr[-1]:
         return True


    return isIn(char, aStr[1:-1])

tests = {
    ('a', ''): False,
    ('m', 'aeegkmovz'): True,
    ('x', 'cffhhjkmmnorrswxyyy'): True,
    ('l', 'abcjjlprrrvwx'): True,
    ('w', 'cdefgjrvwyyz'): True,
    ('b', 'aabbdefgilmmrstuxxxx'): True,
    ('m', 'cqw'): False,
    ('m', 'cdenrrtvxzz'): False,
    ('o', 'abceikloqrssttuuwwyy'): True,
    ('k', 'aabchijkkkllnsvx'): True

}
    

# ------------------ boiler plate

f = isIn


for args, expected in tests.items():
        s = f(*args)
        # assert
        try:
            assert s == expected
            print("✅: success - {1} expected and {0} received".format(
                s,
                expected,
            ))
        except AssertionError:
            msg = "❌: error:\n\texpected: {1}\n\treceived: {0}. {2} ".format(
                s,
                expected,
                args
            )
            sys.exit(msg)