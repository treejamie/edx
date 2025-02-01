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

print("Longest substring in alphabetical order is: {0}".format(answer))