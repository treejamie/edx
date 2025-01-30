"""
Assume s is a string of lower case characters.

Write a program that prints the number of times the string 'bob' occurs in s.

For example, if s = 'azcbobobegghakl', then your program should print
"""

s = 'azcbobobegghakl'
bob_count = 0

for i, maybe_bob in enumerate(s):
	if s[i:i+3] == 'bob':
		bob_count += 1


print("Number of times bob occurs is: {0}".format(bob_count))