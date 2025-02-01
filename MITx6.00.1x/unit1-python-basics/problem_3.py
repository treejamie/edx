import sys

"""
Assume s is a string of lower case characters.

Write a program that prints the longest substring of s in which the letters occur in alphabetical order.
For example, if s = 'azcbobobegghakl', then your program should print


Longest substring in alphabetical order is: beggh

In the case of ties, print the first substring. For example, if s = 'abcbcd', then your program should print

Longest substring in alphabetical order is: abc

Note: This problem may be challenging.
We encourage you to work smart.
	- If you've spent more than a few hours on this problem,
	- we suggest that you move on to a different part of the course.
	- If you have time, come back to this problem after you've had a break and cleared your head.

"""

def solution(s):

	answers = [] # the stash for the answers
	wip = ''     # work in progress

	for i, char in enumerate(s):

		# next_char: 
		# I could have caught the exception
		# but the class has not covered that yet
		if len(s) -1 != i:          # this is fugly
			next_char = s[ i + 1 ]  # and so is this
		else:
			next_char = ''

		# we are always adding to the WIP in all cases
		wip += char

		# if char is greater than append to answers, and reset wip
		if char > next_char:
			answers.append(wip)
			wip = ''


	# what is the longest thing in the answers?
	longest = max([len(x) for x in answers])

	# return the first largest thing
	answer = [x for x in answers if len(x) >= longest][0]
	return answer



tests ={
	'azcbobobegghakl': 'beggh',
	'rikcgzkbes': 'cgz',
	'psygsuarkxvoedyuymv': 'psy',
	'abcdefghijklmnopqrstuvwxyz': 'abcdefghijklmnopqrstuvwxyz',
	'bhogrgkjbd': 'bho',
	'paflivqzpjtfkebavrnhibje': 'afl'
}

for string, expected in tests.items():
	result = solution(string)
        # assert
	try:
		assert result == expected
		print("✅: success {0} - {1} expected and {2} received".format(
			string,
			expected,
			result
		))
	except AssertionError:
		msg = "❌: error in {0}:\n\texpected: {1}\n\treceived: {2} ".format(
			string,
			expected,
			result
		)
		sys.exit(msg)	

