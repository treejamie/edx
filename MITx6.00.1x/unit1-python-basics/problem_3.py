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
s = 'azcbobobegghakl'

# define a longest seen
longest = ''

# define a maybe longest
maybe_longest = ''

# stick to while and for loops as that is what we've has been using so far
for i in range(len(s)):

	if len(maybe_longest) > len(longest):
		longest = maybe_longest

	maybe_longest = ''
	outer = s[i]
	foo = s[i::]

	for j in range(len(foo)):
		# if this is zero loop, special case
		if j == 0:
			prv = outer
			maybe_longest = prv
		else:
			prv = foo[j]

		# define next, catch index error
		try:
			nxt = foo[j + 1]
		except IndexError:
			pass

		# if current less than next, we are alphabetic
		if prv <= nxt:
			# add to maybe longest
			maybe_longest += nxt
		else:
			# reset and move on
			break

print("Longest substring in alphabetical order is: {0}".format(longest))