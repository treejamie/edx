import sys
from ps3_hangman import isWordGuessed, getGuessedWord



#
#
# boilerplate DIY testing
test2 = {
    ('e', 'i', 'k', 'p', 'r', 's'): ("apple", '_ pp_ e'),
    ('e', 'l', 'p', 'p', 'a'): ("apple", 'apple'),
}
target2 = getGuessedWord

print("testing: ", target2.__name__, "---------")

for args, bits in test2.items():

    word = bits[0]
    expected = bits[1]

    result = target2(word, args)

    try:
        assert result == expected
        print("✅: SUCCESS - {1} expected and {0} received".format(
            result,
            expected,
        ))
    except AssertionError:
        msg = "🛥️ FAILBOAT:\n\texpected: {1}\n\treceived: {0} ".format(
            result,
            expected,
        )
        sys.exit(msg)


test1 = {
    ('e', 'i', 'k', 'p', 'r', 's'): ("apple", False),
    ('e', 'l', 'p', 'p', 'a'): ("apple", True),
}
target1 = isWordGuessed

print("testing: ", target1.__name__, "---------")

for args, bits in test1.items():

    word = bits[0]
    expected = bits[1]

    result = target1(word, args)

    try:
        assert result == expected
        print("✅: success - {1} expected and {0} received".format(
            result,
            expected,
        ))
    except AssertionError:
        msg = "❌: error:\n\texpected: {1}\n\treceived: {0} ".format(
            result,
            expected,
        )
        sys.exit(msg)