"""
Assume s is a string of lower case characters.

Write a program that counts up the number of vowels contained in the string s.
Valid vowels are: 'a', 'e', 'i', 'o', and 'u'.

For example, if s = 'azcbobobegghakl', your program should print:


Number of vowels: 5

"""


s = 'azcbobobegghakl'
v = []

for x in s:
	if x in 'aeiou':
		v.append(x)



print("Number of vowels:", len(v))